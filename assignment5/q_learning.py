import gym
import pandas as pd
import numpy as np
env = gym.make('NChain-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n))

new_Q = np.ones_like(Q)

# learning rate / also slip chance
allowed_steps = 100
nr_episodes = 1000

alfa = 0.1
# discount factor
gamma = 0.95

for episode in range(nr_episodes):
    old_state = env.reset()
    # how many steps are the agent allowed to go?
    for t in range(allowed_steps):
        # Get best action based on Q matrix
        action = np.argmax(Q[old_state, :])
        # Step with that action
        new_state, reward, done, info = env.step(action)
        # update Q value for old state following policy
        Q[old_state][action] += alfa * \
            (reward + gamma * max(Q[new_state, :]) - Q[old_state][action])
        
        old_state = new_state
    
    


print("\n******** Q solution ********\n")
print("Q = \n", Q)

print("\n******** Policy ********************")
print("(forward,backward) = (0,1)\n")

print(np.argmax(Q, axis=1), "\n")