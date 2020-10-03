from mdp_general import valueIteration

state = {0:[0, 1], 1:[0, 1], 2:[0, 1], 3:[0, 1], 4:[0, 1]}
rewards = [
    [0, 2],
    [0, 2],
    [0, 2],
    [0, 2],
    [10, 2]
]
# Method for returning the new state given an action and a state 
def getNewState(state, action):
    return {
        0: state + 1 if state < 4 else state,
        1: 0
    }[action]

def chainCalculateActionValue(state, action, vCandidate):
    oppositeAction = abs(1-action)
    newState = getNewState(state, action)
    slipState = getNewState(state, oppositeAction)
    return 0.8*(rewards[state][action] + 0.95*vCandidate[newState]) + 0.2*(rewards[state][oppositeAction] + 0.95*vCandidate[slipState])





print(valueIteration(state, chainCalculateActionValue))