import numpy as np
import gym

env = gym.make('NChain-v0')

#Q = np.zeros((env.observation_space.n, env.action_space.n))

v_prev = np.zeros(env.observation_space.n)
v_curr = np.ones_like(v_prev)
v_actions = np.zeros_like(v_prev)

#v_prev = np.zeros((env.observation_space.n, env.action_space.n))
#v_curr = np.ones_like(v_prev)

rewards = np.array([
    [0, 2],
    [0, 2],
    [0, 2],
    [0, 2],
    [10, 2]
])

action_space_size = env.action_space.n
state_space_size = env.observation_space.n

# slip chance is 0.2
slip = 0.2
alfa = 1-slip
epsilon = 0.95

def getNewState(state, action):
    return {
        0: state + 1 if state < 4 else state,
        1: 0
    }[action]


def calculateActionValue(state,action):
    slip_action = abs(action-1)
    next_state = getNewState(state, action)
    slip_state = getNewState(state, slip_action)

    return alfa * (rewards[state][action] + epsilon*v_prev[next_state]) + (
                1-alfa) * (rewards[state][slip_action] + epsilon * v_prev[slip_state])


while not np.allclose(v_prev, v_curr, atol=0.001):
    v_prev = np.copy(v_curr)
    for state in range(state_space_size):
        actionValues = [calculateActionValue(state,action) for action in range(action_space_size)]
        best_action = np.argmax(actionValues)
        v_curr[state] = actionValues[best_action]
        v_actions[state] = best_action

print("\n******** Candidate solution ********\n")
print(v_curr)
#
print("\n******** Policy ********************")
print("(forward,backward) = (0,1)\n")
print(v_actions, "\n")