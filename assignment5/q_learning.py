import gym
import pandas as pd
import numpy as np
import random
env = gym.make('NChain-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n))

new_Q = np.ones_like(Q)

# learning rate / also slip chance
nr_episodes = 10000

epsilon = 0.5

alfa = 0.1
# discount factor
gamma = 0.95

for episode in range(nr_episodes):
    old_state = env.reset()
    # how many steps are the agent allowed to go?
    done = False
    if(episode % 1000 == 0):
        print("new episode", episode)
    while done == False:
        # decide action based on coinflip
        if (random.uniform(0,1) < epsilon):
            action = env.action_space.sample()
        else:
            # Get best action based on Q matrix
            action = np.argmax(Q[old_state, :])
        # Step with that action
        new_state, reward, done, info = env.step(action)
        # update Q value for old state following policy
        Q[old_state][action] += alfa * \
            (reward + gamma * np.max(Q[new_state, :]) - Q[old_state][action])
        
        old_state = new_state
    
    


print("\n******** Q solution ********\n")
print("Q = \n", Q)

print("\n******** Policy ********************")
print("(forward,backward) = (0,1)\n")
print(np.argmax(Q, axis=1), "\n")

print("\n******** V *************************")
print(np.max(Q,axis=1))