# These are all the possible directions the agent can move to
# I use them as tuples in order to make the app smaller without the use of any strings
WEST       = (-1,0)
NORTH_WEST = (-1,-1)
NORTH      = (0,-1)
NORTH_EAST = (1,-1)
EAST       = (1,0)
SOUTH_EAST = (1,1)
SOUTH      = (0,1)
SOUTH_WEST = (-1,1)


DIRECTIONS = [ WEST, NORTH_WEST, NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST]

# Speed and Air influence variables
SPEED = [1, 2, 3]
AIR   = [-2, -1, 0, 1, 2]


# These colors define the states that a node can have
RESET    = (255, 255, 255) # White Color
BARRIER  = (0,   0,   0)   # Black Color
AGENT1   = (211, 211, 211) # Lightgrey Color
AGENT2   = (169, 169, 169) # Darkgrey Color
TRAIL1   = (255, 165, 0)   # Orange Color
TRAIL2   = (255, 0,   0)   # Red Color
START1   = (0,   150, 0)   # Green Color
END1     = (0,   100, 0)   # Dark Green Color
START2   = (0,   150, 255) # Bright Blue Color
END2     = (0,   0,   255) # Blue Color
GREY     = (128, 128, 128)

# These are the rewards for each Node according to the type
START_REWARD  = -0.01
NORMAL_REWARD = -0.1
BARRIER_REWARD = -0.5
BEST_REWARD   = 15


# These are all the possible actions an agent can perform
ACTIONS =[(NORTH, 1), (NORTH,2), (NORTH,3), (NORTH_EAST, 1), (NORTH_EAST,2), (NORTH_EAST,3),
          (EAST, 1),  (EAST,2),  (EAST,3),  (SOUTH_EAST, 1), (SOUTH_EAST,2), (SOUTH_EAST,3),
          (SOUTH, 1), (SOUTH,2), (SOUTH,3), (SOUTH_WEST, 1), (SOUTH_WEST,2), (SOUTH_WEST,3),
          (WEST, 1),  (WEST,2),  (WEST,3),  (NORTH_WEST, 1), (NORTH_WEST,2), (NORTH_WEST,3)]


# These are the variables for the policy that the AGENT is going to follow
NUM_EPISODES          = 1000
MAX_STEPS_PER_EPISODE = 100
LEARNING_RATE         = 0.01    # This is the α parameter
DISCOUNT_RATE         = 1       # This is the γ parameter
LAMDA                 = 0.65    # This is the λ parameter


EXPLORATION_RATE      = 1      #
MAX_EXP_RATE          = 1      #         Those variables are used for the
MIN_EXP_RATE          = 0.01   #         Epsilon Greedy Strategy
EXPLORATION_DECAY_RATE= 0.001  #