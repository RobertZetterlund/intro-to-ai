import numpy as np
import gym
import random
import time
from IPython.display import clear_output

env = gym.make("NChain-v0")

action_space_size = env.action_space.n
state_space_size = env.observation_space.n

q_table = np.zeros((state_space_size, action_space_size))

num_episodes = 1000
max_steps_per_episode = 100

## alfa
learning_rate = 0.1
## gamma
discount_rate = 0.95

## epsilon
exploration_rate = 1

max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001


rewards_all_episodes = []

for episode in range(num_episodes):
    state = env.reset()
    done = False
    rewards_current_episode = 0

    for step in range(max_steps_per_episode): 

    # Exploration-exploitation trade-off
        exploration_rate_threshold = random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(q_table[state,:]) 
        else:
            action = env.action_space.sample()
        

        new_state, reward, done, info = env.step(action)

        # Update Q-table for Q(s,a)
        q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
        learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))

        state = new_state
        rewards_current_episode += reward

        if done == True: 
            break

    # Exploration rate decay
    exploration_rate = min_exploration_rate + \
    (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episode)
    
    rewards_all_episodes.append(rewards_current_episode)


## print the q table
print("\n******** Q table ********\n")
print(q_table)

print("\n******** Policy ********\n")
print(np.argmax(q_table, axis=1))