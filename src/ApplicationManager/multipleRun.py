import math, random, time
import numpy as np
import pandas as pd
import pygame
from src.Grid.grid import draw, gridReset, make_grid
from src.Grid.grid2 import start_end_pos
from src.Grid.node import Node
from src.Environment.environment import getAir, getSpeed, getSteps, stochasticMovement, updateExploration
from src.Environment.variables import AGENT1, TRAIL1, START1, END1, AGENT2, TRAIL2, START2, END2, MAX_STEPS_PER_EPISODE
from src.Agent.agent import Agent, makeQTable, makeHeatMap
from src.ApplicationManager.eGreedyRun import eGreedyMultiple
from src.ApplicationManager.mcTDRun import mcTdMultiple



def multipleRun(episodes, total_rows, rate, q_type):
    # Some global Variables
    airList1 = []
    rewards1 = []
    reward_from_episodes1 = []
    airList2 = []
    rewards2 = []
    reward_from_episodes2 = []


    # Initialize the grid variables
    width = 600
    total_rows = 20
    theGrid = make_grid(width, total_rows)
    start1, start2, end1, end2 = start_end_pos(theGrid, width, total_rows)


    # Initialize agents and their heatmaps
    heatMap1 = makeHeatMap(total_rows)
    agent1 = Agent(start1.row, start1.column, airList1, rewards1, reward_from_episodes1, AGENT1, TRAIL1, START1, END1, heatMap1)
    heatMap2 = makeHeatMap(total_rows)
    agent2 = Agent(start2.row, start2.column, airList2, rewards2, reward_from_episodes2, AGENT2, TRAIL2, START2, END2, heatMap2)

    # Initialize the elegibility_tables, the q_tables
    q_table1 = makeQTable(total_rows)
    q_table2 = makeQTable(total_rows)
    el_table1 = makeQTable(total_rows)
    el_table2 = makeQTable(total_rows)


    for episode in range(episodes):
        counter = 0
        run1 = True
        run2 = True

        # Environment rendering/reseting
        window = pygame.display.set_mode((width, width))
        pygame.display.set_caption(f'Multiple-Agent Environment for {episodes} episodes')
        gridReset(theGrid, total_rows)
        theGrid[start1.row][start1.column].set_state(START1)
        theGrid[start2.row][start2.column].set_state(START2)
        theGrid[end1.row][end1.column].set_state(END1)
        theGrid[end2.row][end2.column].set_state(END2)
        

        # Agents and state-action lists reseting
        agent1 = Agent(start1.row, start1.column, airList1, rewards1, reward_from_episodes1, AGENT1, TRAIL1, START1, END1, heatMap1)
        agent2 = Agent(start2.row, start2.column, airList2, rewards2, reward_from_episodes2, AGENT2, TRAIL2, START2, END2, heatMap2)
        SAList1 = []
        SAList2 = []


        # The agent runs in the grid for the maximum steps based on the q-learning type
        if q_type == "e-greedy":
            eGreedyMultiple(window, theGrid, width, total_rows, rate, run1, run2, agent1, agent2, q_table1, q_table2, el_table1, el_table2, SAList1, SAList2, episode, counter)
        elif q_type == "mc-td":
            mcTdMultiple(window, theGrid, width, total_rows, rate, run1, run2, agent1, agent2, q_table1, q_table2, el_table1, el_table2, SAList1, SAList2, episode, counter)

        # Update the exploration rate after each episode
        rate = updateExploration(episode)


    print(sum(reward_from_episodes1))
    print(sum(reward_from_episodes2))

    # Export the q_tables
    q_table1.to_csv("Data/agent1.csv", sep=",")
    q_table2.to_csv("Data/agent2.csv", sep=",")

    # Export the rewards from each episode
    reward1_df = pd.DataFrame(agent1.reward_all_ep)
    reward2_df = pd.DataFrame(agent2.reward_all_ep)
    reward1_df.to_csv("Data/rewards1.csv", sep=",", index=False)
    reward2_df.to_csv("Data/rewards2.csv", sep=",", index=False)

    # Export the heatmaps of each agent
    agent1.heatMap.to_csv("Data/heatmap1.csv", sep=",")
    agent2.heatMap.to_csv("Data/heatmap2.csv", sep=",")