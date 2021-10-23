import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#                            Preprocessing Functions                          #
# Get the average reward per number of episodes
def getAvgReward(number, list1):
    result = []
    summedList = getSum(number, list1)
    for i in range(len(summedList)):
        result.append(summedList[i] / number)
    return result


# Get the sum of rewards per number of episodes
def getSum(number, list1):
    result = []
    sum = 0

    if type(list1[0]) == list:
        for i in range(len(list1)):
            if i % number == 0:
                result.append(sum)
                sum = 0
            else:
                sum += list1[i][0]
    else:
        for i in range(len(list1)):
            if i % number == 0:
                result.append(sum)
                sum = 0
            else:
                sum += list1[i]
    return result


# Compute the reward taken by both agents for every episode
def getFinalRewards(list1, list2):
    finalList = []

    for k in range(len(list1)):
        finalList.append(list1[k][0] + list2[k][0])

    return finalList


# Add the heatMap values of both agents
def sumHeatMap(heatMap1, heatMap2):
    sumHeatMap = heatMap1.add(heatMap2, fill_value=0)
    return sumHeatMap



#                            Ploting Functions                          #
# Plot each agents rewards per episode
def plotRewardsAgents(rewards1, rewards2):
    plt.plot(rewards1, "r", label="E-Greedy")
    plt.plot(rewards2, "b", label="Monte-Carlo-Temporal Difference")
    plt.xlabel("Number of Episodes")
    plt.ylabel("Reward per episode")
    plt.title("Rewards acquired by each agent")
    plt.legend()
    plt.savefig("analytics/indAgents.png")

# Plot the rewards of both agents per episode
def plotRewardsBothAgents(rewards1, kind):
    plt.plot(rewards1, label="Agent 1")
    plt.xlabel("Number of Episodes")
    plt.ylabel("Reward per episode")
    plt.title("Rewards acquired by agent")
    plt.legend()
    plt.savefig(f"analytics/Agents_{kind}.png")




#                            Heatmap Functions                          #
# Initialize the heatmap based on the data
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw={}, cbarlabel="", **kwargs):

    if not ax: ax = plt.gca()

    # Plot the heatmap and create colorbar
    im = ax.imshow(data, **kwargs)
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-0, ha="right", rotation_mode="anchor")
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="K")
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


# Annotate the heatmap (Write the number of steps in the heatmap cell)
def annotate_heatmap(im, data=None, valfmt="{x:.1f}", textcolors=("black")):

    if not isinstance(data, (list, np.ndarray)): data = im.get_array()
    kw = dict(horizontalalignment="center", verticalalignment="center")
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel" color the text
    # in valfmt(data[i,j]) -> valfmt(data[j,i])
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors)
            # Change the i,j with j,i
            text = im.axes.text(j, i, valfmt(data[i, j], None), fontsize=6, **kw)
            texts.append(text)

    return texts


# Function the manages the two functions above to simplify their usage
def heatMap(data, name):

    # Define the data to be imported to the heatMap by the 
    statesX = data.iloc[:,0].values.tolist()  # Get the states for the heatmap
    statesY = []
    for col in data.columns:
        statesY.append(col)
    statesY.pop(0)
    semiFinalData = data.iloc[:, 1:].values.tolist()
    finalData = np.transpose(semiFinalData)


    # Convert the lists to numpy arrays for the heatmap function
    statesArrayX = np.asarray(statesX)
    statesArrayY = np.asarray(statesY)
    finalDataArray = np.asarray(finalData)

    fig, ax = plt.subplots()
    im, cbar = heatmap(finalDataArray, statesArrayX, statesArrayY, ax=ax, cmap="YlOrRd", cbarlabel= "HeatMap of Agents Movement")
    texts = annotate_heatmap(im, valfmt="{x:}")
    plt.tight_layout()
    plt.savefig(f"analytics/heatmap_{name}.png")



#                            Bar Functions                          #

# Define the intervals that we are going to use to plot the bar plot 
# (we take average of "number" of episodes at the time)
def defineXTicks(lenght, number):
    initial = []
    result = []

    # Find the intervals
    for i in range(lenght // number):
        if i != 0:
            initial.append((initial[i-1][1], number + i*number))
        else:
            initial.append((0, number + i*number))

    # Transform the tuple intervals to strings for the BarPlot function
    for i in range(len(initial)):
        st = '-'.join(map(str, initial[i]))
        result.append(st)

    return result


# Create the Bar Plot with the initial data and the number of episodes we are grouping the data
def BarPlot(list1, list2, number):

    # Define the data that are going to be used (rewards of agents and number of episodes)
    agent1 = getAvgReward(number, list1)
    agent2 = getAvgReward(number, list2)

    # Initialize the figure and set position of bar on X axis
    fig = plt.subplots()
    br1 = np.arange(len(agent1))
    br2 = [x + 0.20 for x in br1]

    # Make the plot
    plt.bar(br1, agent1, color ='r', width = 0.20, edgecolor ='black', label ='Agent1')
    plt.bar(br2, agent2, color ='b', width = 0.20, edgecolor ='black', label ='Agent2')

    # Adding Xticks
    plt.xlabel(f'Average reward per {number} episodes',fontsize = 10)
    plt.ylabel('Rewards received by the agent', fontsize = 10)
    xTikcs = defineXTicks(len(list1), number)
    plt.xticks([r + 0.20 for r in range(len(agent1))], xTikcs)

    plt.legend(loc='lower right')
    plt.savefig("analytics/BarPlot.png")


