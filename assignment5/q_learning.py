import gym
import pandas as pd
import numpy as np
env = gym.make('NChain-v0', slip=0)

Q = np.zeros((env.observation_space.n, env.action_space.n))
#
#epsilon = 0.9
# learning rate / also slip chance
alfa = 0.2
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
        # update Q value for old state following policy
        Q[old_state][action] = (1-alfa) * Q[old_state][action] + alfa * \
            (reward + gamma * max(Q[new_state, :]) - Q[old_state][action])
        
        old_state = new_state


print("\n******** Q solution ********\n")
print("Q = \n", Q)

print("\n******** Policy ********************")
print("(forward,backward) = (0,1)\n")

print(np.argmax(Q, axis=1), "\n")
# env.close()