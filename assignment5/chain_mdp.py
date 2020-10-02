import numpy as np
import gym

env = gym.make('NChain-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n))

V_prev = np.copy(Q)
V_curr = np.ones_like(Q)

rewards = np.array([
    [0, 2],
    [0, 2],
    [0, 2],
    [0, 2],
    [10, 2]
])

action_space_size = env.action_space.n
state_space_size = env.observation_space.n

alfa = 1
epsilon = 0.9

V_new = np.copy(V_curr)

while not np.allclose(V_prev, V_curr, atol=0.001):
    V_new = np.copy(V_curr)
    V_prev = np.copy(V_curr)
    for state in range(state_space_size):
        for action in range(action_space_size):
            not_action = abs(action-1)

            V_new[state][action] = alfa * (rewards[state][action] + epsilon*V_prev[state][action]) + (
                1-alfa) * (rewards[state][not_action] + epsilon * V_prev[state][action])

    v_curr = np.copy(V_new)
    


print(v_curr)