import numpy as np
import gym

env = gym.make('NChain-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n))

v_prev = np.copy(Q)
v_curr = np.ones_like(Q)

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
alfa = 0.8
epsilon = 0.9

while not np.allclose(v_prev, v_curr, atol=0.001):
    v_prev = np.copy(v_curr)
    for state in range(state_space_size):
        for action in range(action_space_size):
            not_action = abs(action-1)

            v_curr[state][action] = alfa * (rewards[state][action] + epsilon*v_prev[state][action]) + (
                1-alfa) * (rewards[state][not_action] + epsilon * v_prev[state][not_action])
    
print("\n******** Candidate solution ********\n")
print(v_curr)

print("\n******** Policy ********************")
print("(forward,backward) = (0,1)\n")
print(np.argmax(v_curr, axis=1), "\n")