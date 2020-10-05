import gym
import pandas as pd
import numpy as np
import random
env = gym.make('NChain-v0', slip=0.8)

Q = np.zeros((env.observation_space.n, env.action_space.n))
Qcopy = np.ones((env.observation_space.n, env.action_space.n))
#
epsilon = 0.5
# learning rate
alfa = 0.1
# discount factor
gamma = 0.95

iteration = 0
# To make the algorithm converge
alfadecay = 0.999
while not np.allclose(Q,Qcopy, atol=0.01):
    iteration += 1
    old_state = env.reset()
    alfa *= alfadecay
    done = False
    Qcopy = Q.copy() 
    while not done:
        action = env.action_space.sample() if random.random() < epsilon else np.argmax(Q[old_state,:])
    
        new_state, reward, done, info = env.step(action)
        # update Q value for old state following policy

        Q[old_state][action] += alfa * \
            (reward + gamma * np.max(Q[new_state, :]) - Q[old_state][action])
        
        old_state = new_state

    if(iteration % 100 == 0):
        diff = np.subtract(Q, Qcopy)
        diff = np.absolute(diff)
        print("Iteration", iteration, "Max diff: ", diff.max())


print("\n******** Q solution ********\n")
print("Q = \n", Q)

print("\n******** Policy ********************")
print("(forward,backward) = (0,1)\n")
print(np.argmax(Q, axis=1), "\n")





# env.close()
