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


def eGreedyMultiple(window, theGrid, width, total_rows, rate, run1, run2, agent1, agent2, q_table1, q_table2, el_table1, el_table2, SAList1, SAList2, episode, counter):

    for steps in range(MAX_STEPS_PER_EPISODE):
    
        draw(window, theGrid, width, total_rows)
        expl_threshold = random.uniform(0,1)

        if expl_threshold > rate:
            if run1 == True: 
                run1 = agent1.movePolicy(theGrid, total_rows, q_table1, el_table1, SAList1, counter, episode, "e-greedy")
            if run2 == True: 
                run2 = agent2.movePolicy(theGrid, total_rows, q_table2, el_table2, SAList2, counter, episode, "e-greedy")
        else:
            if run1 == True: 
                run1 = agent1.move(theGrid, total_rows, q_table1, el_table1, SAList1, counter, episode, "e-greedy")
            if run2 == True: 
                run2 = agent2.move(theGrid, total_rows, q_table2, el_table2, SAList2, counter, episode, "e-greedy")
        if run1 == False and run2 == False: break
        counter +=1

def eGreedySingle(window, theGrid, width, total_rows, rate, run, agent, q_table1, el_table1, SAList1, episode, counter):

    for steps in range(MAX_STEPS_PER_EPISODE):
    
        draw(window, theGrid, width, total_rows)
        expl_threshold = random.uniform(0,1)

        if expl_threshold > rate:
            if run == True: 
                run = agent.movePolicy(theGrid, total_rows, q_table1, el_table1, SAList1, counter, episode, "e-greedy")
        else:
            if run == True: 
                run = agent.move(theGrid, total_rows, q_table1, el_table1, SAList1, counter, episode, "e-greedy")
        
        if run == False: break
        counter +=1