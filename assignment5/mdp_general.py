import numpy as np

'''
Performs a value iteration

states should be a dictionary contain the states and the possible values at those states

calculateActionValue should be a function that given the state, the action and the current vCandidate,
will calculate the action value. The vCandidate will be a dictionary with the states as the keys and 
the current values of those states as the values. 

Returns the converged value function. It will be a dictionary of the form {state:(best action(s), expected value)}
'''
def valueIteration(states, calculateActionValue):
    vCandidate = {s:(None, 0) for s in states.keys()}
    lastCandidate = {s:(None,1) for s in states.keys()}

    while not np.allclose([value for _,(_,value) in vCandidate.items()], [value for _,(_,value) in lastCandidate.items()]):
        lastCandidate = vCandidate.copy()
        for state in states.keys():
            actions = [(action, calculateActionValue(state, action, {s:value for  s, (_, value) in vCandidate.items()})) for action in states[state]]
            maxActionValue = max([value for _,value in actions])
            bestActions = [(action, value) for action,value in actions if value == maxActionValue]
            #Update the new candidate with the max action value and the actions giving that value
            vCandidate[state] = ([action for action,_ in bestActions], maxActionValue)

    return vCandidate


