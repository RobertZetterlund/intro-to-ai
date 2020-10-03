from mdp_general import valueIteration

state = {0:["N", "E"], 1:["N", "E", "W"], 2:["N", "W"], 3:["N", "E", "S"], 4:["N", "E", "S", "W"], 5:["N", "W", "S"], 6:["S", "E"], 7:["S", "E", "W"], 8:["S", "W"]}

rewards = {0:0, 1:0, 2:0, 3:0, 4:10, 5:0, 6:0, 7:0, 8:0}



def getNewState(state, action):
    if action == "N": return state + 3
    if action == "S": return state - 3
    if action == "E": return state + 1
    if action == "W": return state - 1

def gridCalculateActionValue(state, action, vCandidate):
    newState = getNewState(state, action)
    return 0.8*(rewards[newState] + 0.9*vCandidate[newState]) + 0.2*(rewards[state] + 0.9*vCandidate[state])


print(valueIteration(state, gridCalculateActionValue))

