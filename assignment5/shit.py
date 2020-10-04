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

slip = 0.2

rewards = np.array([
    [0, 2],
    [0, 2],
    [0, 2],
    [0, 2],
    [10, 2]
])


V = np.array([61.34916509, 64.86097309, 69.48177309, 75.56177309, 83.56177309])


def getNewState(state, action):
    return {
        0: state + 1 if state < 4 else state,
        1: 0
    }[action]


def getQpi(V, state, action):
    s_sum = 0
    not_action = abs(action-1)

    new_state = getNewState(state, action)
    slip_state = getNewState(state, not_action)

    # for each possible future state
    s_sum += (1-slip) * (rewards[state][action] + gamma*V[new_state])
    s_sum += (slip) * (rewards[state][not_action] + gamma*V[slip_state])

    return s_sum

def getOptimalQ():
    slip = 0.2
    for state in range(5):
        for action in range(2):
            not_action = abs(action-1)
            next_state = getNewState(state,action)
            slip_state = getNewState(state,not_action)
            
            Q[state][action] += slip * (rewards[state][not_action] + gamma * V[slip_state])
            Q[state][action] += (1-slip) * (rewards[state][action] + gamma * V[next_state])


    print(Q)


# for episode in range(nr_episodes):
#    old_state = env.reset()
#    # how many steps are the agent allowed to go?
#    for t in range(allowed_steps):
#        # Get best action based on Q matrix
#        action = np.argmax(Q[old_state, :])
#        # Step with that action
#        new_state, reward, done, info = env.step(action)
#        # update Q value for old state following policy
#        Q[old_state][action] += alfa * \
#            (reward + gamma * max(Q[new_state, :]) - Q[old_state][action])
#
#        old_state = new_state
#
#    V = np.max(Q, axis=1)
#
#    Qpi = [getQpi(V,state,action) for (state,action) in enumerate(np.argmax(Q, axis=1))]
#
#    print("\n qpi:",Qpi)
#    print("\n v: ", V)
#    print("**********************************'")
#    if(np.allclose(Qpi, V, atol=0.1)):
#        break
#
'''
for episode in range(nr_episodes):
    Q = np.copy(new_Q)
    for state in range(5):
        for action in range(2):
            reward = rewards[state][action]
            new_state = getNewState(state, action)
            new_Q[state][action] += alfa * \
                (reward + gamma * max(Q[new_state, :]) - Q[state][action])


print("\n******** Q solution ********\n")
print("Q = \n", Q)

print("\n******** Policy ********************")
print("(forward,backward) = (0,1)\n")

print(np.argmax(Q, axis=1), "\n")
'''
getOptimalQ()