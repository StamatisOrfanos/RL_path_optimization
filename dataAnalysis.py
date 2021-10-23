import pandas as pd
import random as rd
import math
import matplotlib.pyplot as plt
from numpy import transpose
from src.DataAnalysis.dataManager import plotRewardsAgents, getFinalRewards, getAvgReward, heatMap, sumHeatMap, getSum, BarPlot, plotRewardsBothAgents


# # Import the reward data for both agents for the Monte-Carlo & Temporal Difference (firstly run for rewards1 and then for rewards2)
mcTDMreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/1st/rewards2.csv")
mcTDMreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/2nd/rewards2.csv")
mcTDMreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/3rd/rewards2.csv")
mcTDMreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/4th/rewards2.csv")
mcTDMreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/5th/rewards2.csv")
mcTDMreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/6th/rewards2.csv")
mcTDMreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/7th/rewards2.csv")
mcTDMreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/8th/rewards2.csv")
mcTDMreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/9th/rewards2.csv")
mcTDMreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/10th/rewards2.csv")


# # Import the reward data for both agents for the E-Greedy (firstly run for rewards1 and then for rewards2)
EMreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/1st/rewards2.csv")
EMreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/2nd/rewards2.csv")
EMreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/3rd/rewards2.csv")
EMreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/4th/rewards2.csv")
EMreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/5th/rewards2.csv")
EMreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/6th/rewards2.csv")
EMreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/7th/rewards2.csv")
EMreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/8th/rewards2.csv")
EMreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/9th/rewards2.csv")
EMreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/10th/rewards2.csv")


# # Add the data to one reward
# mcTdsumRewards = sum([mcTDreward1, mcTDreward2, mcTDreward3, mcTDreward4, mcTDreward5, mcTDreward6, mcTDreward7, mcTDreward8, mcTDreward9, mcTDreward10])
# EsumRewards    = sum([Ereward1, Ereward2, Ereward3, Ereward4, Ereward5, Ereward6, Ereward7, Ereward8, Ereward9, Ereward10])

# # Divide by 10 each value of the dataframe to get the average
# mcTdDividedRewards = mcTdsumRewards/10
# EDividedRewards = EsumRewards/10

# # Transform to list in order to be passed as parameters
# mcTDList = mcTdDividedRewards.values.tolist()
# EList = EDividedRewards.values.tolist()

# # Plot tha data per number of episodes
# mcTDfinal = getAvgReward(10000, mcTDList)
# Efinal = getAvgReward(10000, EList)
# plotRewardsAgents(Efinal, mcTDfinal)



# Import the heatmap data for both agents for Monte-Carlo (firstly run for heatmap1 and then for heatmap2)
mcTDheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/1st/heatmap2.csv")
mcTDheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/2nd/heatmap2.csv")
mcTDheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/3rd/heatmap2.csv")
mcTDheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/4th/heatmap2.csv")
mcTDheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/5th/heatmap2.csv")
mcTDheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/6th/heatmap2.csv")
mcTDheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/7th/heatmap2.csv")
mcTDheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/8th/heatmap2.csv")
mcTDheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/9th/heatmap2.csv")
mcTDheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/mc-td/10th/heatmap2.csv")


# # Import the heatmap data for both agents for E-Greedy (firstly run for heatmap1 and then for heatmap2)
Eheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/1st/heatmap2.csv")
Eheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/2nd/heatmap2.csv")
Eheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/3rd/heatmap2.csv")
Eheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/4th/heatmap2.csv")
Eheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/5th/heatmap2.csv")
Eheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/6th/heatmap2.csv")
Eheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/7th/heatmap2.csv")
Eheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/8th/heatmap2.csv")
Eheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/9th/heatmap2.csv")
Eheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/MultiAgent/e-greedy/10th/heatmap2.csv")



# # Add the data to one heatmap
# mcTdsumHeatmap = sum([mcTDheatmap1, mcTDheatmap2, mcTDheatmap3, mcTDheatmap4, mcTDheatmap5, mcTDheatmap6, mcTDheatmap7, mcTDheatmap8, mcTDheatmap9, mcTDheatmap10])
# EsumHeatmap    = sum([Eheatmap1, Eheatmap2, Eheatmap3, Eheatmap4, Eheatmap5, Eheatmap6, Eheatmap7, Eheatmap8, Eheatmap9, Eheatmap10])

# # Divide by 10 each value of the dataframe to get the average
# mcTdDividedHeatmap = mcTdsumHeatmap/10
# EDividedHeatmap = EsumHeatmap/10

# # Turn to integer type
# finalMCTD = mcTdDividedHeatmap.astype(int)
# finalE = EDividedHeatmap.astype(int)

# # Plot tha data per number of episodes
# heatMap(finalMCTD, "Monte-Carlo-Temporal Difference Heatmap")
# heatMap(finalE, "E-Greedy Heatmap")











####################################################################################
# Single Agent stable
ESreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/1st/rewards1.csv").values.tolist()
ESreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/2nd/rewards1.csv").values.tolist()
ESreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/3rd/rewards1.csv").values.tolist()
ESreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/4th/rewards1.csv").values.tolist()
ESreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/5th/rewards1.csv").values.tolist()
ESreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/6th/rewards1.csv").values.tolist()
ESreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/7th/rewards1.csv").values.tolist()
ESreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/8th/rewards1.csv").values.tolist()
ESreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/9th/rewards1.csv").values.tolist()
ESreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/10th/rewards1.csv").values.tolist()


MCTDSreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/1st/rewards1.csv").values.tolist()
MCTDSreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/2nd/rewards1.csv").values.tolist()
MCTDSreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/3rd/rewards1.csv").values.tolist()
MCTDSreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/4th/rewards1.csv").values.tolist()
MCTDSreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/5th/rewards1.csv").values.tolist()
MCTDSreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/6th/rewards1.csv").values.tolist()
MCTDSreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/7th/rewards1.csv").values.tolist()
MCTDSreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/8th/rewards1.csv").values.tolist()
MCTDSreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/9th/rewards1.csv").values.tolist()
MCTDSreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/10th/rewards1.csv").values.tolist()

# # Add the data to one reward
# mcTdsumRewards = sum([MCTDSreward1, MCTDSreward2, MCTDSreward3, MCTDSreward4, MCTDSreward5, MCTDSreward6, MCTDSreward7, MCTDSreward8, MCTDSreward9, MCTDSreward10])
# EsumRewards    = sum([ESreward1, ESreward2, ESreward3, ESreward4, ESreward5, ESreward6, ESreward7, ESreward8, ESreward9, ESreward10])

# # Divide by 10 each value of the dataframe to get the average
# mcTdDividedRewards = mcTdsumRewards/10
# EDividedRewards = EsumRewards/1

# # Transform to list in order to be passed as parameters
# mcTDList = mcTdDividedRewards.values.tolist()
# EList = EDividedRewards.values.tolist()

# # Plot tha data per number of episodes
# mcTDfinal = getAvgReward(2500, mcTDList)
# Efinal = getAvgReward(2500, EList)
# plotRewardsAgents(Efinal, mcTDfinal)


ESheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/1st/heatmap.csv")
ESheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/2nd/heatmap.csv")
ESheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/3rd/heatmap.csv")
ESheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/4th/heatmap.csv")
ESheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/5th/heatmap.csv")
ESheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/6th/heatmap.csv")
ESheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/7th/heatmap.csv")
ESheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/8th/heatmap.csv")
ESheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/9th/heatmap.csv")
ESheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/e-greedy/10th/heatmap.csv")


MCTDSheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/1st/heatmap.csv")
MCTDSheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/2nd/heatmap.csv")
MCTDSheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/3rd/heatmap.csv")
MCTDSheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/4th/heatmap.csv")
MCTDSheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/5th/heatmap.csv")
MCTDSheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/6th/heatmap.csv")
MCTDSheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/7th/heatmap.csv")
MCTDSheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/8th/heatmap.csv")
MCTDSheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/9th/heatmap.csv")
MCTDSheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/stable/mc-td/10th/heatmap.csv")


# # Add the data to one heatmap
# mcTdsumHeatmap = sum([MCTDSheatmap1, MCTDSheatmap2, MCTDSheatmap3, MCTDSheatmap4, MCTDSheatmap5, MCTDSheatmap6, MCTDSheatmap7, MCTDSheatmap8, MCTDSheatmap9, MCTDSheatmap10])
# EsumHeatmap    = sum([ESheatmap1, ESheatmap2, ESheatmap3, ESheatmap4, ESheatmap5, ESheatmap6, ESheatmap7, ESheatmap8, ESheatmap9, ESheatmap10])

# # Divide by 10 each value of the dataframe to get the average
# mcTdDividedHeatmap = mcTdsumHeatmap/10
# EDividedHeatmap = EsumHeatmap/10

# # Turn to integer type
# finalMCTD = mcTdDividedHeatmap.astype(int)
# finalE = EDividedHeatmap.astype(int)

# # Plot tha data per number of episodes
# heatMap(finalMCTD, "Monte-Carlo-Temporal Difference Heatmap")
# heatMap(finalE, "E-Greedy Heatmap")












####################################################################################

# Single Agent slow movement
EGreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/1st/rewards1.csv").values.tolist()
EGreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/2nd/rewards1.csv").values.tolist()
EGreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/3rd/rewards1.csv").values.tolist()
EGreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/4th/rewards1.csv").values.tolist()
EGreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/5th/rewards1.csv").values.tolist()
EGreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/6th/rewards1.csv").values.tolist()
EGreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/7th/rewards1.csv").values.tolist()
EGreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/8th/rewards1.csv").values.tolist()
EGreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/9th/rewards1.csv").values.tolist()
EGreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/10th/rewards1.csv").values.tolist()


McTdreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/1st/rewards1.csv").values.tolist()
McTdreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/2nd/rewards1.csv").values.tolist()
McTdreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/3rd/rewards1.csv").values.tolist()
McTdreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/4th/rewards1.csv").values.tolist()
McTdreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/5th/rewards1.csv").values.tolist()
McTdreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/6th/rewards1.csv").values.tolist()
McTdreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/7th/rewards1.csv").values.tolist()
McTdreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/8th/rewards1.csv").values.tolist()
McTdreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/9th/rewards1.csv").values.tolist()
McTdreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/10th/rewards1.csv").values.tolist()


# # Add the data to one reward
# mcTdsumRewards = sum([McTdreward1, McTdreward2, McTdreward3, McTdreward4, McTdreward5, McTdreward6, McTdreward7, McTdreward8, McTdreward9, McTdreward10])
# EsumRewards    = sum([EGreward1, EGreward2, EGreward3, EGreward4, EGreward5, EGreward6, EGreward7, EGreward8, EGreward9, EGreward10])

# # Divide by 10 each value of the dataframe to get the average
# mcTdDividedRewards = mcTdsumRewards/10
# EDividedRewards = EsumRewards/10

# # Transform to list in order to be passed as parameters
# mcTDList = mcTdDividedRewards.values.tolist()
# EList = EDividedRewards.values.tolist()

# # Plot tha data per number of episodes
# mcTDfinal = getAvgReward(10000, mcTDList)
# Efinal = getAvgReward(10000, EList)
# plotRewardsAgents(Efinal, mcTDfinal)

EGheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/1st/heatmap.csv")
EGheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/2nd/heatmap.csv")
EGheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/3rd/heatmap.csv")
EGheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/4th/heatmap.csv")
EGheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/5th/heatmap.csv")
EGheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/6th/heatmap.csv")
EGheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/7th/heatmap.csv")
EGheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/8th/heatmap.csv")
EGheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/9th/heatmap.csv")
EGheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/e-greedy/10th/heatmap.csv")

McTdheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/1st/heatmap.csv")
McTdheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/2nd/heatmap.csv")
McTdheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/3rd/heatmap.csv")
McTdheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/4th/heatmap.csv")
McTdheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/5th/heatmap.csv")
McTdheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/6th/heatmap.csv")
McTdheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/7th/heatmap.csv")
McTdheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/8th/heatmap.csv")
McTdheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/9th/heatmap.csv")
McTdheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/slowmovement/mc-td/10th/heatmap.csv")


# Add the data to one heatmap
mcTdsumHeatmap = sum([McTdheatmap1, McTdheatmap2, McTdheatmap3, McTdheatmap4, McTdheatmap5, McTdheatmap6, McTdheatmap7, McTdheatmap8, McTdheatmap9, McTdheatmap10])
EsumHeatmap    = sum([EGheatmap1, EGheatmap2, EGheatmap3, EGheatmap4, EGheatmap5, EGheatmap6, EGheatmap7, EGheatmap8, EGheatmap9, EGheatmap10])

# Divide by 10 each value of the dataframe to get the average
mcTdDividedHeatmap = mcTdsumHeatmap/10
EDividedHeatmap = EsumHeatmap/10

# Turn to integer type
finalMCTD = mcTdDividedHeatmap.astype(int)
finalE = EDividedHeatmap.astype(int)

# Plot tha data per number of episodes
heatMap(finalMCTD, "Monte-Carlo-Temporal Difference Heatmap")
heatMap(finalE, "E-Greedy Heatmap")











####################################################################################

# Single Agent fast movement
EGFreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/1st/rewards1.csv").values.tolist()
EGFreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/2nd/rewards1.csv").values.tolist()
EGFreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/3rd/rewards1.csv").values.tolist()
EGFreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/4th/rewards1.csv").values.tolist()
EGFreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/5th/rewards1.csv").values.tolist()
EGFreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/6th/rewards1.csv").values.tolist()
EGFreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/7th/rewards1.csv").values.tolist()
EGFreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/8th/rewards1.csv").values.tolist()
EGFreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/9th/rewards1.csv").values.tolist()
EGFreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/10th/rewards1.csv").values.tolist()


McTdFreward1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/1st/rewards1.csv").values.tolist()
McTdFreward2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/2nd/rewards1.csv").values.tolist()
McTdFreward3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/3rd/rewards1.csv").values.tolist()
McTdFreward4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/4th/rewards1.csv").values.tolist()
McTdFreward5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/5th/rewards1.csv").values.tolist()
McTdFreward6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/6th/rewards1.csv").values.tolist()
McTdFreward7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/7th/rewards1.csv").values.tolist()
McTdFreward8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/8th/rewards1.csv").values.tolist()
McTdFreward9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/9th/rewards1.csv").values.tolist()
McTdFreward10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/10th/rewards1.csv").values.tolist()


# # Add the data to one reward
# mcTdsumRewards = sum([McTdFreward1, McTdFreward2, McTdFreward3, McTdFreward4, McTdFreward5, McTdFreward6, McTdFreward7, McTdFreward8, McTdFreward9, McTdFreward10])
# EsumRewards    = sum([EGFreward1, EGFreward2, EGFreward3, EGFreward4, EGFreward5, EGFreward6, EGFreward7, EGFreward8, EGFreward9, EGFreward10])

# # Divide by 10 each value of the dataframe to get the average
# mcTdDividedRewards = mcTdsumRewards/10
# EDividedRewards = EsumRewards/10

# # Transform to list in order to be passed as parameters
# mcTDList = mcTdDividedRewards.values.tolist()
# EList = EDividedRewards.values.tolist()

# # Plot tha data per number of episodes
# mcTDfinal = getAvgReward(2500, mcTDList)
# Efinal = getAvgReward(2500, EList)
# plotRewardsAgents(Efinal, mcTDfinal)




EGFheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/1st/heatmap.csv")
EGFheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/2nd/heatmap.csv")
EGFheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/3rd/heatmap.csv")
EGFheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/4th/heatmap.csv")
EGFheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/5th/heatmap.csv")
EGFheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/6th/heatmap.csv")
EGFheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/7th/heatmap.csv")
EGFheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/8th/heatmap.csv")
EGFheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/9th/heatmap.csv")
EGFheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/e-greedy/10th/heatmap.csv")

McTdFheatmap1  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/1st/heatmap.csv")
McTdFheatmap2  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/2nd/heatmap.csv")
McTdFheatmap3  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/3rd/heatmap.csv")
McTdFheatmap4  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/4th/heatmap.csv")
McTdFheatmap5  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/5th/heatmap.csv")
McTdFheatmap6  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/6th/heatmap.csv")
McTdFheatmap7  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/7th/heatmap.csv")
McTdFheatmap8  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/8th/heatmap.csv")
McTdFheatmap9  = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/9th/heatmap.csv")
McTdFheatmap10 = pd.read_csv("/home/stamatiosorfanos/Documents/ΠΑΠΕΙ/Πτυχιακή/E17113_final/Data/SingleAgent/fastmovement/mc-td/10th/heatmap.csv")


# # Add the data to one heatmap
# mcTdsumHeatmap = sum([McTdFheatmap1, McTdFheatmap2, McTdFheatmap3, McTdFheatmap4, McTdFheatmap5, McTdFheatmap6, McTdFheatmap7, McTdFheatmap8, McTdFheatmap9, McTdFheatmap10])
# EsumHeatmap    = sum([EGFheatmap1, EGFheatmap2, EGFheatmap3, EGFheatmap4, EGFheatmap5, EGFheatmap6, EGFheatmap7, EGFheatmap8, EGFheatmap9, EGFheatmap10])

# # Divide by 10 each value of the dataframe to get the average
# mcTdDividedHeatmap = mcTdsumHeatmap/10
# EDividedHeatmap = EsumHeatmap/10

# # Turn to integer type
# finalMCTD = mcTdDividedHeatmap.astype(int)
# finalE = EDividedHeatmap.astype(int)

# # Plot tha data per number of episodes
# heatMap(finalMCTD, "Monte-Carlo-Temporal Difference Heatmap")
# heatMap(finalE, "E-Greedy Heatmap")