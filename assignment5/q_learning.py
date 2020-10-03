import gym
import pandas as pd
import numpy as np
import random
env = gym.make('NChain-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n))


#
epsilon = 0.1
# learning rate
alfa = 0.1
# discount factor
gamma = 0.95

actionDict = {
    0: "Forward",
    1: "Backward"
}

for i_episode in range(1000):
    old_state = env.reset()
    done = False
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(Q[old_state]) # Exploit learned values

        action = env.action_space.sample()
        new_state, reward, done, info = env.step(action)

    
        # given performing action from state observation, we get reward... so
        #move = actionDict[action]
        #print("prevstate: ", prev_state, " move: ", move, "state: ", state, " reward: ", reward)
        Q[old_state][action] = Q[old_state][action] + alfa * \
            (reward + gamma * max(Q[new_state, :]) - Q[old_state][action])

        old_state = new_state

        

print(Q)
# env.close()
