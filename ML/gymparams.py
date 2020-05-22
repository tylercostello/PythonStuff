import gym
env = gym.make('MountainCarContinuous-v0')
nA = env.action_space
print(nA)
