import gym
import numpy as np
#import matplotlib.pyplot as plt
import copy
from FinalSigSoftScratchNN import NN

#Hyperparameters
NUM_EPISODES = 1000000
LEARNING_RATE = 1
GAMMA = 0.99

# Create gym and seed numpy
env = gym.make('CartPole-v0')
nA = env.action_space.n
#print(nA)
np.random.seed(1)

# Init weight
newNN=NN(4,1,2)
#w = np.random.rand(4, 2)

# Keep stats for final print of graph
episode_rewards = []

# Our policy that maps state to action parameterized by w
def policy(state):
	return newNN.feedforward(state)

# Vectorized softmax Jacobian
"""
def softmax_grad(softmax):
    s = softmax.reshape(-1,1)
    #print((np.diagflat(s) - np.dot(s, s.T)).shape)
    return np.diagflat(s) - np.dot(s, s.T)
"""
# Main loop
# Make sure you update your weights AFTER each episode
for e in range(NUM_EPISODES):

	state = env.reset()[None,:]

	grads1 = []
	grads2 = []
	rewards = []
	probsCache=0
	# Keep track of game score to print
	score = 0

	while True:

		# Uncomment to see your model train in real time (slower)
		#env.render()

		# Sample from policy and take action in environment
		#print(state)
		#2d array of 4 values
		probs = policy(state)
		#print(probs[0])
		#print(probs)
		#2d array of 2 values
		probsCache=probs
		#print(nA)
		#na=2
		#print(probs[0])
		#print(probs)
		#1d array of 2 values
		#(2)
		#first value in probs is prob of zero, second is prob of one
		#action=0
		#print(probs)
		#print(probs[0])
		action = np.random.choice(nA,p=probs[0])
		#choose from array randomly based on their probs
		#print(action)
		#0 or 1
		next_state,reward,done,_ = env.step(action)
		next_state = next_state[None,:]
		#print(action)
		# Compute gradient and save with reward in memory for our weight updates

		#print(softmax_grad(probs))
		#print()
		#print(action)
		d1=newNN.dw1(action)
		d2=newNN.dw2(action)
		#dsoftmax = softmax_grad(probs)[action,:]
		#print(dsoftmax.size)
		#gradients in the column of the actions
		#there are as many columns as actions
		#print(dsoftmax)
		dlog1 = d1 / probs[0,action]
		dlog2 = d2 / probs[0,action]
		#print(dlog.size)
		grad1 = dlog1
		grad2 = dlog2
		#print(grad.size)
		#print("State")
		#print(state)
		#print(state.T)
		grads1.append(grad1)
		grads2.append(grad2)
		rewards.append(reward)

		score+=reward

		# Dont forget to update your old state to the new state
		state = next_state

		if done:
			break

	# Weight update
	for i in range(len(grads1)):

		# Loop through everything that happend in the episode and update towards the log policy gradient times **FUTURE** reward
		#sum is v(t)
		 newNN.addw1(LEARNING_RATE * grads1[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])]))
		#print(LEARNING_RATE * grads[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])]))
	for i in range(len(grads2)):

		# Loop through everything that happend in the episode and update towards the log policy gradient times **FUTURE** reward
		#sum is v(t)
		 newNN.addw2(LEARNING_RATE * grads2[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])]))
		#print(LEARNING_RATE * grads[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])]))

	# Append for logging and print
	episode_rewards.append(score)
	if e%100==0:
		print("EP: " + str(e) + " Score: " + str(score))
		print(probsCache)

#plt.plot(np.arange(NUM_EPISODES),episode_rewards)
#plt.show()
env.close()
