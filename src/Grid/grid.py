import math, random
import pygame, time
import tkinter as tk
from src.Environment.variables import GREY, RESET, AGENT1, AGENT2, TRAIL1, TRAIL2, START1, START2, END1, END2, START_REWARD, BEST_REWARD, BARRIER
from src.Grid.node import Node

# SOS:
# https://stackoverflow.com/questions/47361769/pygame-seems-to-flip-rows-and-columns


# Grid object (list of lists of Nodes)
def make_grid(width, total_rows):
    grid = []
    gap = width // total_rows

    for i in range(total_rows):
        grid.append([]) # Make the rows of the grid
        for j in range(total_rows):
            node = Node(i, j, gap, total_rows) # Each node has a row, column, gap=node-width
            grid[i].append(node)

    return grid


# Draw both the horizontal and the certical lines of the grid
def draw_grid(window, width, total_rows):
    gap = width // total_rows

    for i in range(total_rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap)) # Horizontal Lines 
        for j in range(total_rows):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width)) # Vertical Lines


# Draw the pygame window every time the episode ends
def draw(window, grid, width, total_rows):
    window.fill(RESET)

    for row in grid:
        for node in row:
            node.draw_node(window)
    
    draw_grid(window, width, total_rows)
    pygame.display.update()


# Reset the environment after the episode end
def gridReset(grid, total_rows):

    for i in range(total_rows):
        for j in range(total_rows):
            
            if grid[i][j].color == AGENT1 or grid[i][j].color == AGENT2 or grid[i][j].color == TRAIL1 or grid[i][j].color == TRAIL2:
                grid[i][j].set_state(RESET)


def manhattan_distance(node1, node2):
    return abs((node1.x - node2.x )) + abs((node1.y - node2.y))


# Creates barriers in random Nodes inside the grid (not the edges)
def defineBarriers(grid, total_rows):
    num_barriers = int(math.sqrt(total_rows))

    for i in range(num_barriers):
        grid[random.randint(1, total_rows-2)][random.randint(1, total_rows-2)].set_state(BARRIER)

# Creates barriers in random Nodes inside the grid (not the edges)
def clearBarriers(grid, total_rows):
     for i in range(total_rows):
        for j in range(total_rows):
            
            if grid[i][j].color == AGENT1 or grid[i][j].color == BARRIER:
                grid[i][j].set_state(RESET)