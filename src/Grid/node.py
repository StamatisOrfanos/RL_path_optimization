import math, random
import pygame 
from pygame import draw
from src.Environment.variables import RESET, NORMAL_REWARD


class Node:
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row * width 
        self.y = column * width
        self.color = RESET
        self.reward = NORMAL_REWARD
        self.width = width
        self.total_rows = total_rows


    # Draw the node to the grid
    def draw_node(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    # Set the state of a node to the right object
    def set_state(self, state):
        self.color = state

    # Get the coordinates of a node
    def get_coordinates(self):
        return self.x , self.y