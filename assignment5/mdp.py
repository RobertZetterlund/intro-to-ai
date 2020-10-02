import numpy as np

# Starting matrixes. We represents our v candidate as a 2d vector where each element is a tuple 
# containing the best expected value and the best action(s) to take.
vCandidate = [[(0, "E/N"),(0, "E/N/W"),(0, "N/W")], [(0, "N/E/S"),(0, "N/E/S/W"),(0, "N/W/S")], [(0, "E/S"),(0, "E/S/W"),(0, "W/S")]]
lastCandidate= [[(-1, ""), (-1, ""), (-1, "")], [(-1, ""), (-1, ""), (-1, "")], [(-1, ""), (-1, ""), (-1, "")]]
rewards = [[0,0,0], [0,10,0], [0,0,0]]

# Method returning the possible actions to take given a state
def getPossibleActions(state):
    directions = []
    if state[0] > 0:
        directions.append("W")
    if state[0] < 2:
        directions.append("E")
    if state[1] > 0:
        directions.append("S")
    if state[1] < 2:
        directions.append("N")
    return directions    
# Method for returning the new state given an action and a state 
def getNewState(state, action):
    return {
        'N': (state[0], state[1]+1),
        'W': (state[0]-1, state[1]),
        'S': (state[0], state[1]-1),
        'E': (state[0]+1, state[1]),
    }[action]

# Returns the reward at the given state state
def getReward(state):
    return rewards[state[1]][state[0]]

# Returns the value of the current value function candidate at a given state
def getValueOfVCandidate(state):
    return vCandidate[state[1]][state[0]][0]
#Calculates the expected value of taking a certain action
def calculateActionValue(state, action):
    newState = getNewState(state, action)
    return 0.8*(getReward(newState) + 0.9*getValueOfVCandidate(newState)) + 0.2*(getReward(state) + 0.9*getValueOfVCandidate(state))

#Returns the action values of a candidate matrix
def onlyActionValues(matrix):
        return list(map(lambda column: list(map(lambda item: item[0], column)), matrix))
    
#Util method for copying a matrix
def copyMatrix(matrix):
    newMatrix= [[0, 0, 0],[0, 0 ,0],[0,0,0]]
    for row in range(0,3):
        for col in range(0,3):
            newMatrix[row][col] = matrix[row][col]
    return newMatrix  

#The algorithm

# Check if algorithm is converging
while not np.allclose(onlyActionValues(vCandidate),onlyActionValues(lastCandidate), atol=0.001):
    newCandidate = copyMatrix(vCandidate)
    lastCandidate = copyMatrix(vCandidate)
    for row in range(0,3):
        for col in range(0,3):
            state = (col, row)
            #Get all actions and their expected value
            actions = [(calculateActionValue(state, action), action) for action in getPossibleActions(state)]
            #Calculate what the maximum action value is
            maxActionValue = max(actions, key=lambda x:x[0])[0]
            #Collect the best actions, that is, the actions with an action value equal to the max action value
            bestActions = [(value, action) for value, action in actions if value == maxActionValue]
            #Update the new candidate with the max action value and the actions giving that value
            newCandidate[row][col] = (maxActionValue, '/'.join([actionTuple[1] for actionTuple in bestActions]))
            
    #Update our candidate!
    vCandidate = copyMatrix(newCandidate)
    

for line in vCandidate[::-1]:
    print(*line)