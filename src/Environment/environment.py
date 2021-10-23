import random
import pandas as pd
import numpy as np
from src.Environment.variables import *

# Checks if the next node is in the grid
def check_borders(row, column, total_rows):
    if row < 0 or row > total_rows-1 or column < 0 or column > total_rows-1:
        return False
    else:
        return True

# This function gives us the speed that the agent is going to have
def getSpeed():
    speed = random.choices([SPEED[0], SPEED[1], SPEED[2]], (10, 80, 10), k=1)
    return speed[0]


# This funciton is going to give us the air influnce of the environment
def getAir(num, airList):
    # If this is the first step choose 100% randomly 
    if len(airList) == 0:
        weightedAir = [ [AIR[0], 20], [AIR[1], 20], [AIR[2], 20], [AIR[3], 20], [AIR[4], 20] ]
        population = [val for val, cnt in weightedAir for i in range(cnt)]
        air = random.choice(population)
        airList.append([num, air])
    # If this is every 5th step choose randomly, but with proximity given the air before
    elif num % 5 == 0:
        if airList[num-1][1] == -2:
            weightedAir = [ [AIR[0], 20], [AIR[1], 60], [AIR[2], 20]]
        elif airList[num-1][1] == -1:
            weightedAir = [ [AIR[0], 30], [AIR[1], 20], [AIR[2], 30], [AIR[3], 20]]
        elif airList[num-1][1] == 0:
            weightedAir = [ [AIR[0], 10], [AIR[1], 30], [AIR[2], 20], [AIR[3], 30], [AIR[4], 10]]
        
        elif airList[num-1][1] == 1:
            weightedAir = [ [AIR[1], 20], [AIR[2], 30], [AIR[3], 20], [AIR[4], 30]]
        
        elif airList[num-1][1] == 2:
            weightedAir = [ [AIR[2], 20], [AIR[3], 60], [AIR[4], 20]]
        population = [val for val, cnt in weightedAir for i in range(cnt)]
        air = random.choice(population)
        airList.append([num, air])
    
    # Else get the same value as before
    else:
        airList.append([num, airList[num-1][1]])
    return airList


# This function will give us the steps taken in the grid by the plane
def getSteps(speed, air):
    if speed + air > 3: steps = 3
    elif speed + air <= 0: steps = 1
    else: steps = speed + air
    
    return steps


# This function will simulate the stochastic environment of the project for the directions and the steps
def stochasticMovement(direction, steps, num, airList):

    if direction == WEST:
        initialDir = [DIRECTIONS[n] for n in (7, 0, 1)]
    elif direction == NORTH_WEST:
        initialDir = [DIRECTIONS[n] for n in (0, 1, 2)]
    elif direction == NORTH:
        initialDir = [DIRECTIONS[n] for n in (1, 2, 3)]
    elif direction == NORTH_EAST:
        initialDir = [DIRECTIONS[n] for n in (2, 3, 4)]
    elif direction == EAST:
        initialDir = [DIRECTIONS[n] for n in (3, 4, 5)]
    elif direction == SOUTH_EAST:
        initialDir = [DIRECTIONS[n] for n in (4, 5, 6)]
    elif direction == SOUTH:
        initialDir = [DIRECTIONS[n] for n in (5, 6, 7)]
    elif direction == SOUTH_WEST:
        initialDir = [DIRECTIONS[n] for n in (6, 7, 0)]
    finalDirection = random.choices(initialDir, (5, 90, 5), k=1)

    # If we exploit the env we already know the steps that we want to take, but we add the
    # stochastic element and in the other case we randomly get the steps taken
    if steps != 0:
        if steps == 1:
            finalSteps = random.choices((1,2,3), (90, 5, 5), k=1)
        elif steps == 2:
            finalSteps = random.choices((1,2,3), (5, 90, 5), k=1)
        else:
            finalSteps = random.choices((1,2,3), (5, 5, 90), k=1)
        return finalDirection[0], finalSteps[0]
    else:
        speed = getSpeed()
        air = getAir(num, airList)
        finalSteps = getSteps(speed, air[num][1])
        return finalDirection[0], finalSteps


# Check if there is a barrier node in the next 1-3 steps and update the q_table 
def check_barriers(row, column, grid, q_table, steps, direction, total_rows):

    # Define all the possible states that the agent can go based on the direction and steps
    finalRow    = row + steps * direction[0]
    finalColumn = column + steps * direction[1]

    # Define all the possible states that the agent can land on
    state1 = (row + 1 * direction[0], column + 1 * direction[1])
    state2 = (row + 2 * direction[0], column + 2 * direction[1])
    state3 = (row + 3 * direction[0], column + 3 * direction[1])

    # Make the boolean values to check if we are in the grid still to avoid exceptions  
    value1 =  check_borders(state1[0],state1[1], total_rows)
    value2 =  check_borders(state2[0], state2[1], total_rows)
    value3 =  check_borders(state3[0],state3[1], total_rows)

    if value1 and grid[state1[0]][state1[1]].color == BARRIER and steps >=1:
        q_table.loc[state1, :] = BARRIER_REWARD
        finalRow    = row
        finalColumn = column

    if value2 and grid[state2[0]][state2[1]].color == BARRIER and steps >=2:
        q_table.loc[state2, :] = BARRIER_REWARD
        finalRow    = row + 1 * direction[0]
        finalColumn = column + 1 * direction[1]

    if  value3 and grid[state3[0]][state3[1]].color == BARRIER and steps >=3:
        q_table.loc[state3, :] = BARRIER_REWARD
        finalRow    = row + 2 * direction[0]
        finalColumn = column + 2 * direction[1]

    return finalRow, finalColumn



# As the episodes increase the agent knows more about the environment so it can exploit the info better
# and get quicker at the goal.
def updateExploration(episode):
    newRate = MIN_EXP_RATE + (MAX_EXP_RATE - MIN_EXP_RATE) * np.exp(-EXPLORATION_DECAY_RATE*episode)
    return newRate