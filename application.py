from src.Environment.variables import EXPLORATION_RATE
from src.ApplicationManager.singleRun import singleRun
from src.ApplicationManager.multipleRun import multipleRun
from datetime import datetime


def main(episodes, total_rows, numAgents, q_type):
    print("Welcome to my Reinforcement Learning application for Trajectory Optimization")
    if numAgents == 1:
        singleRun(episodes, total_rows, EXPLORATION_RATE, q_type)
    else:
        multipleRun(episodes, total_rows, EXPLORATION_RATE, q_type)


if __name__ == "__main__":
    main(1, 20, 1, "e-greedy")
