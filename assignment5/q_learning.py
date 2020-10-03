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

for i_episode in range(100000):
    old_state = env.reset()

    for t in range(5):
        action = env.action_space.sample()
        new_state, reward, done, info = env.step(action)

        # given performing action from state observation, we get reward... so
        #move = actionDict[action]
        #print("prevstate: ", prev_state, " move: ", move, "state: ", state, " reward: ", reward)

        Q[old_state][action] = Q[old_state][action] + alfa * \
            (reward + gamma * max(Q[new_state, :]) - Q[old_state][action])

        old_state = new_state

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

print(Q)
# env.close()
