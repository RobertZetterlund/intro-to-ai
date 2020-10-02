import gym
import pandas as pd
import numpy as np
env = gym.make('NChain-v0')


qtable = pd.DataFrame(data=[[0, 0], [0, 0], [0, 0], [0, 0], [
                      0, 0]], columns=["Stay", "Step"])


Q = np.zeros((env.observation_space.n, env.action_space.n))

print(Q)

epsilon = 0.9
alfa = 0.7
gamma = 0.99


print(qtable)

actionDict = {
    0: "Step",
    1: "Stay"
}


def createEpsilonGreedyPolicy(Q, epsilon, num_actions):
    """
    Creates an epsilon-greedy policy based
    on a given Q-function and epsilon.

    Returns a function that takes the state
    as an input and returns the probabilities
    for each action in the form of a numpy array
    of length of the action space(set of possible actions).
    """
    def policyFunction(state):

        Action_probabilities = np.ones(num_actions,
                dtype=float) * epsilon / num_actions

        best_action = np.argmax(Q[state])
        Action_probabilities[best_action] += (1.0 - epsilon)
        return Action_probabilities

    return policyFunction


for i_episode in range(5):
    observation = env.reset()

    policy = createEpsilonGreedyPolicy(qtable, epsilon, env.action_space.n)

    for t in range(5):
        print(observation)
        action = env.action_space.sample()
        move = actionDict[action]
        notmove = actionDict[abs(action-1)]

        observation, reward, done, info = env.step(action)

        # given performing action from state observation, we get reward... so
        print("state: ", observation, " move: ", move, " reward: ", reward)

        qtable[move][observation] = qtable[move][observation] * (1-alfa) + alfa*(reward + max(qtable[notmove][observation], qtable[move][observation]))


        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

print(qtable)
# env.close()
