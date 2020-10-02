import gym
import pandas as pd
import numpy as np
env = gym.make('NChain-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n))

print(Q)

epsilon = 0.9
alfa = 0.1
gamma = 0.95

actionDict = {
    0: "Forward",
    1: "Backward"
}

for i_episode in range(5):
    prev_state = env.reset()

    for t in range(5):
        #print(state)
        action = env.action_space.sample()
        move = actionDict[action]
        notmove = actionDict[abs(action-1)]

        state, reward, done, info = env.step(action)

        # given performing action from state observation, we get reward... so
        print("state: ", state, " move: ", move, " reward: ", reward)

        Q[prev_state][action] = Q[prev_state][action] + alfa*(reward + gamma * max(Q[state][abs(action-1)], Q[state][action]) - Q[prev_state][action])

        prev_state = state

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

print(Q)
# env.close()
