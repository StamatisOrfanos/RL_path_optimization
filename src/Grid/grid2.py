import math, random
import pygame, time
import tkinter as tk
from src.Environment.variables import START1, START2, END1, END2, START_REWARD, BEST_REWARD
from src.Grid.node import Node

# Multi-agent Environment


# Get the start and end node for each agent and insert them to the grid
def start_end_pos(grid, width, total_rows):
    start_node1, end_node1, start_node2, end_node2 = checkForPos(grid, total_rows)

    for i in range(total_rows):
        for j in range(total_rows):

            if (i,j) == (start_node1.row, start_node1.column):
                grid[i][j].set_state(START1)

            if (i,j) == (end_node1.row, end_node1.column):
                grid[i][j].set_state(END1)

            if (i,j) == (start_node2.row, start_node2.column):
                grid[i][j].set_state(START2)

            if (i,j) == (end_node2.row, end_node2.column):
                grid[i][j].set_state(END2)

    return start_node1, start_node2, end_node1, end_node2


# Get the start and end positions for both agents
def checkForPos(grid, total_rows):

    top    = (0, random.randint(0, total_rows-1))
    bottom = (total_rows-1, random.randint(0, total_rows-1))
    left   = (random.randint(0, total_rows-1), 0)
    right  = (random.randint(0, total_rows-1), total_rows-1)

    locations = [top, bottom, left, right]

    # Get the startign and ending positions for the 2 agents 
    start1, end1, start2, end2 = pos_setUp(locations)


    # Set the start and end node in case they are close the first time around
    start_node1 = grid[start1[0]][start1[1]]
    start_node2 = grid[start2[0]][start2[1]]

    end_node1   = grid[end1[0]][end1[1]]
    end_node2   = grid[end2[0]][end2[1]]


    # Set the rewards of those two nodes
    start_node1.reward = START_REWARD
    start_node2.reward = START_REWARD

    end_node1.reward = BEST_REWARD
    end_node2.reward = BEST_REWARD

    return start_node1, end_node1, start_node2, end_node2


# Give each start and end a certain node at the borders of the grid
def pos_setUp(location):

    start_agent1 = random.choices(location, weights=[1,1,1,1], k=1)[0]
    index =  location.index(start_agent1)
    location.pop(index)

    end_agent1   = random.choices(location, weights=[1,1,1], k=1)[0]
    index =  location.index(end_agent1)
    location.pop(index)

    start_agent2 = random.choices(location, weights=[1,1], k=1)[0]
    index =  location.index(start_agent2)
    location.pop(index)

    end_agent2   = random.choices(location, weights=[1], k=1)[0]
    index =  location.index(end_agent2)
    location.pop(index)

    return start_agent1, end_agent1, start_agent2, end_agent2