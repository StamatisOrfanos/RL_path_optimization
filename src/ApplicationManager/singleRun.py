
import math, random, time
import numpy as np
import pandas as pd
import pygame
from src.Grid.grid import draw, gridReset, make_grid, defineBarriers, clearBarriers
from src.Grid.grid1 import start_end_pos
from src.Grid.node import Node
from src.Environment.environment import getAir, getSpeed, getSteps, stochasticMovement, updateExploration
from src.Environment.variables import AGENT1, TRAIL1, START1, END1, AGENT2, TRAIL2, START2, END2, MAX_STEPS_PER_EPISODE
from src.Agent.agent import Agent, makeQTable, makeHeatMap
from src.ApplicationManager.eGreedyRun import eGreedySingle
from src.ApplicationManager.mcTDRun import mcTdSingle



# Single-Agent Environment Application


def singleRun(episodes, total_rows, rate, q_type):
    # Some Usefull Variables
    airList1 = []
    rewards1 = []
    reward_from_episodes1 = []


    # Initialize the grid variables
    width = 600
    total_rows = total_rows
    theGrid = make_grid(width, total_rows)
    start1, end1 = start_end_pos(theGrid, width, total_rows)
    # Commented out for experiments
    # defineBarriers(theGrid, total_rows)


    # Initialize agent and its heatmap
    heatMap= makeHeatMap(total_rows)
    agent1 = Agent(start1.row, start1.column, airList1, rewards1, reward_from_episodes1, AGENT1, TRAIL1, START1, END1, heatMap)

    # Initialize elegibility_table and the q_table
    q_table = makeQTable(total_rows)
    el_table = makeQTable(total_rows)


    for episode in range(episodes):
        if episode == 0:
            defineBarriers(theGrid, total_rows)
        elif episode % 10000 == 0:
            clearBarriers(theGrid, total_rows)
            defineBarriers(theGrid, total_rows)

        counter = 0
        run = True

        # Environment rendering/reseting
        window = pygame.display.set_mode((width, width))
        pygame.display.set_caption(f'Single-Agent Environment for {episodes} episodes')
        gridReset(theGrid, total_rows)
        theGrid[start1.row][start1.column].set_state(START1)
        theGrid[end1.row][end1.column].set_state(END1)

        # Agent and state-action list reseting
        agent1 = Agent(start1.row, start1.column, airList1, rewards1, reward_from_episodes1, AGENT1, TRAIL1, START1, END1, heatMap)
        SAList = []

        # The agent runs in the grid for the maximum steps 
        if q_type == "e-greedy":
            eGreedySingle(window, theGrid, width, total_rows, rate, run, agent1, q_table, el_table, SAList, episode, counter)
        elif q_type == "mc-td":
            mcTdSingle(window, theGrid, width, total_rows, rate, run, agent1, q_table, el_table,  SAList, episode, counter)


        # Update the exploration rate after each episode
        rate = updateExploration(episode)


    print(sum(reward_from_episodes1))

    # Export the q_tables
    q_table.to_csv("Data/agent1.csv", sep=",")

    # Export the rewards from each episode
    reward1_df = pd.DataFrame(agent1.reward_all_ep)
    reward1_df.to_csv("Data/rewards1.csv", sep=",", index=False)

    # Export the heatmaps of each agent
    agent1.heatMap.to_csv("Data/heatmap.csv", sep=",")


