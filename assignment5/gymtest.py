import gym
import pandas as pd
import numpy as np
env = gym.make('NChain-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n))


#
#epsilon = 0.9
# learning rate
alfa = 0.1
# discount factor
gamma = 0.95

actionDict = {
    0: "Forward",
    1: "Backward"
}

for i_episode in range(100):
    prev_state = env.reset()

    for t in range(5):
        action = env.action_space.sample()
        not_action = abs(action-1)

        state, reward, done, info = env.step(action)

        # given performing action from state observation, we get reward... so
        #move = actionDict[action]
        #print("prevstate: ", prev_state, " move: ", move, "state: ", state, " reward: ", reward)

        Q[prev_state][action] = Q[prev_state][action] + alfa*(reward + gamma * max(Q[state][not_action], Q[state][action]) - Q[prev_state][action])

        prev_state = state

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

print(Q)
# env.close()
