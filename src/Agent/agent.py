import math, random, time
import pygame
import numpy as np
import pandas as pd
from src.Grid.grid import draw, make_grid
from src.Grid.node import Node
from src.Environment.variables import BARRIER, BARRIER_REWARD, TRAIL1, TRAIL2, AGENT1, AGENT2, DIRECTIONS, ACTIONS, LEARNING_RATE, DISCOUNT_RATE, LAMDA
from src.Environment.environment import getAir, getSpeed, getSteps, stochasticMovement, check_borders, check_barriers


class Agent:
    def __init__(self, row, column, airList, rewards, reward_all_ep, agent_type, agent_trail, agent_start, agent_end, heatMap):
        self.row = row
        self.column = column
        self.airList = airList
        self.rewards = rewards
        self.reward_all_ep = reward_all_ep
        self.agent_type = agent_type
        self.agent_trail = agent_trail
        self.agent_start = agent_start
        self.agent_end = agent_end
        self.heatMap = heatMap

    def defineBarrier(self):
        if self.agent_trail == TRAIL1: return TRAIL2
        else: return TRAIL1

    def defineAgent(self):
        if self.agent_type == AGENT1: return AGENT2
        else: return AGENT1

    def translate(self):
        if self.agent_type == AGENT1: return "Agent1"
        else: return "Agent2"


    # Get number of barriers or agents in the near area to calculate the reward
    def barrier_counter(self, grid, total_rows):
        miles = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        reward_check = 0

        for i in miles:
            for j in miles:
                if check_borders(self.row + i, self.column + j, total_rows) == False or (i == 0 and j == 0):
                    continue
                if grid[self.row+i][self.column+j].color == self.defineBarrier():
                    reward_check += ( 1 / (abs(i)**2 +abs(j)**2) ) * BARRIER_REWARD
                if grid[self.row+i][self.column+j].color == self.defineAgent():
                    reward_check += BARRIER_REWARD
                if  grid[self.row+i][self.column+j].color == BARRIER:
                    reward_check += ( 1 / (abs(i)**2 +abs(j)**2) ) * BARRIER_REWARD

        return reward_check


    # Update the position of the agent in the grid, the rewards of the agent and the tables of the agent
    def update_position(self, grid, q_table, el_table, saList, numStep, direction, steps, total_rows, episode, moveType, q_type):
        inGrid = True
        newRow = self.row + steps * direction[0]
        newCol = self.column + steps * direction[1]


        if check_borders(newRow, newCol, total_rows):

            # Update the agent position, make the states for the q_table value computation & update heatmap when policy
            finalRow, finalColumn = check_barriers(self.row, self.column, grid, q_table, steps, direction, total_rows)
            state = (self.row, self.column)
            new_state = (finalRow, finalColumn)
            self.row = finalRow
            self.column = finalColumn
            if moveType == "policy" : self.heatMap.loc[new_state] = self.heatMap.at[new_state] + 1

            # Update the reward list and the value of the q_table for the givent state
            negative_reward = self.barrier_counter(grid, total_rows)
            finalReward = negative_reward + grid[finalRow][finalColumn].reward
            self.rewards.append(finalReward)

            # Use the q-learning function that the user specified
            self.q_learning(q_type, numStep, q_table, el_table, saList, direction, steps, state, new_state)


            # Check for the type of the new state (end state/node of grid)
            if grid[finalRow][finalColumn].color == self.agent_end:
                print("I got the max reward sir")
                inGrid = False
            else:
                grid[finalRow][finalColumn].set_state(self.agent_type)
                inGrid = True
        else:
            inGrid = False

        return inGrid



    # Random movement function
    def move(self, grid, total_rows, q_table, el_table, saList, num, episode, q_type):
        direction = random.choice(DIRECTIONS)
        finalDirection, steps = stochasticMovement(direction, 0, num, self.airList)
        num +=1

        # Update the position of the agent
        grid[self.row][self.column].set_state(self.agent_trail)
        inGrid = self.update_position(grid, q_table, el_table, saList, num, finalDirection, steps, total_rows, episode, "random", q_type)

        # Check the agent movement in the grid
        if inGrid == False:
            if num == 1: self.rewards.append(0.0)
            self.reward_all_ep.append(sum(self.rewards))
            self.rewards.clear()
            return False
        else:
            return True



    # Movement based on the agent's policy
    def movePolicy(self, grid, total_rows, q_table, el_table, saList, num, episode, q_type):

        # State of agent to use in the q_table to get the maximun action
        state = (self.row, self.column)
        action = [column for column in q_table if (q_table[column] >= q_table.max(axis=1)[state]).any()]

        # Take a random action of those with the maximum q value for a certain state
        rand = random.randint(0, len(action)-1)
        direction = action[rand][0:1][0]
        steps = action[rand][1:2][0]

        finalDirection, finalSteps = stochasticMovement(direction, steps, num, self.airList)
        num += 1

        # Update the position of the agent
        grid[self.row][self.column].set_state(self.agent_trail)
        inGrid = self.update_position(grid, q_table, el_table, saList, num, finalDirection, finalSteps, total_rows, episode, "policy", q_type)

        if inGrid == False:
            if num == 1: self.rewards.append(0.0)
            self.reward_all_ep.append(sum(self.rewards))
            self.rewards.clear()
            return False
        else:
            return True


    # Q-Learning manager function that defines which q-learning method will be used
    def q_learning(self, qType, current_step, q_table, el_table, stateActionsList, direction, steps, state, new_state):

        if qType == "e-greedy":
            eGreedyQLearning(q_table, self.rewards[current_step-1], state, new_state, direction, steps)

        elif qType == "mc-td":
            state = (self.row, self.column)

            if current_step != 0:
                if len(stateActionsList) >= 2:
                    tdMCQLearning(q_table, el_table, stateActionsList)
                    stateActionsList.append([state, (direction, steps), self.rewards[current_step-1]])
                    stateActionsList.pop(0)
                else:
                    stateActionsList.append([state, (direction, steps), self.rewards[current_step-1]])
            else:
                stateActionsList.append([state, (direction, steps), 0.0])





# Initialize the q_table according to the environment parameters
def makeQTable(total_rows):
    states = []

    for row in range(total_rows):
        for column in range(total_rows):
            states.append((row, column))

    table = pd.DataFrame(0, index=states, columns=ACTIONS)
    table = table.fillna(0)
    return table


# Initialize the heatmap according to the environment parameters
def makeHeatMap(total_rows):
    cols = []
    rows = []
    
    for i in range(total_rows):
        rows.append(i)
        cols.append(i)

    table = pd.DataFrame(0, index=rows, columns=cols)
    table = table.fillna(0)
    return table



# Q-learning function for E-greedy strategy
def eGreedyQLearning(q_table, reward, state, new_state, direction, steps):
    q_table.loc[state, (direction, steps)] = (1-LEARNING_RATE) * q_table.at[state, (direction, steps)] + LEARNING_RATE * (reward + DISCOUNT_RATE * q_table.max(axis=1)[new_state] - q_table.at[state, (direction, steps)])


# Q-Learning function for Hybrid Temporal Difference and Motne Carlo
def tdMCQLearning(q_table, el_table, stateActionsList):

    # Get the both the old and new state action pair with the rewards
    old_SA = stateActionsList[0]
    new_SA = stateActionsList[1]

    # Update the elegibility table and get the TD-error
    el_table.loc[old_SA[0], old_SA[1]] = DISCOUNT_RATE * LEARNING_RATE * el_table.at[old_SA[0], old_SA[1]] + 1
    tdError = new_SA[2] + LAMDA * q_table.at[new_SA[0], new_SA[1]] - q_table.at[old_SA[0], new_SA[1]]

    # Update the q_table value accoring to this formula: Q(s,a) = Q(s,a)+αδtEt(s,a)
    q_table.loc[old_SA[0], old_SA[1]] = q_table.at[old_SA[0], old_SA[1]] + LEARNING_RATE * tdError * el_table.at[old_SA[0], old_SA[1]]