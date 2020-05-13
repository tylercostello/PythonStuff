#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Imports
import numpy as np

# Each row is a training example, each column is a feature  [X1, X2, X3]
import gym
import numpy as np
#import matplotlib.pyplot as plt
import copy

#Hyperparameters
NUM_EPISODES = 10000
LEARNING_RATE = 0.000025
GAMMA = 0.99

# Create gym and seed numpy
env = gym.make('CartPole-v0')
nA = env.action_space.n
#print(nA)
np.random.seed(1)
def sigmoid(t):
	return 1/(1+np.exp(-t))

# Derivative of sigmoid
def sigmoid_derivative(p):
	return p * (1 - p)
def softmax_function(inputs):
	exp = np.exp(inputs)
	return exp/np.sum(exp)
# Class definition

class NeuralNetwork:
	def __init__(self):

		#print(self.input)
		#print(self.input.shape[1])
		self.weights1= np.random.rand(4,4)
		#self.weights1= np.random.rand(self.input.shape[1],4) # considering we have 4 nodes in the hidden layer
		self.weights2 = np.random.rand(4,2)

		self.output = np. zeros(2)

	def feedforward(self,inputs):
		self.layer1 = sigmoid(np.dot(inputs, self.weights1))
		self.layer2 = softmax_function(np.dot(self.layer1, self.weights2))
		return self.layer2

	"""def backprop(self):
		d_weights2 = np.dot(self.layer1.T, 2*(self.y -self.output)*sigmoid_derivative(self.output))
		d_weights1 = np.dot(self.input.T, np.dot(2*(self.y -self.output)*sigmoid_derivative(self.output), self.weights2.T)*sigmoid_derivative(self.layer1))

		self.weights1 += d_weights1
		self.weights2 += d_weights2"""

	def train(self, X, y):
		self.output = self.feedforward()
		self.backprop()
	def wtoc(self):
		return np.concatenate([self.weights1.reshape(-1,1),self.weights2.reshape(-1,1)])
	def ctow(self,newWeights):

		weights1=newWeights[0:self.weights1.size].reshape(4,4)
		weights2=newWeights[self.weights1.size:].reshape(4,2)
# Init weight
NN = NeuralNetwork()
w = NN.wtoc()

# Keep stats for final print of graph
episode_rewards = []

# Our policy that maps state to action parameterized by w

# Vectorized softmax Jacobian
def softmax_grad(softmax):
	s = softmax.reshape(-1,1)
	return np.diagflat(s) - np.dot(s, s.T)

# Main loop
# Make sure you update your weights AFTER each episode
for e in range(NUM_EPISODES):

	state = env.reset()[None,:]

	grads = []
	rewards = []

	# Keep track of game score to print
	score = 0

	while True:
		w = NN.wtoc()
		#probs = policy(state,w)
		probs = NN.feedforward(state)
		action = np.random.choice(nA,p=probs[0])
		next_state,reward,done,_ = env.step(action)
		next_state = next_state[None,:]
		dsoftmax = softmax_grad(probs)[action,:]
		dlog = dsoftmax / probs[0,action]
		grad = state.T.dot(dlog[None,:])
		print("State")
		print(state)
		print(state.T)
		grads.append(grad)
		rewards.append(reward)

		score+=reward
		state = next_state

		if done:
			break

	# Weight update
	for i in range(len(grads)):

		# Loop through everything that happend in the episode and update towards the log policy gradient times **FUTURE** reward
		#sum is v(t)
		w += LEARNING_RATE * grads[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])])

	NN.ctow()
	# Append for logging and print
	episode_rewards.append(score)
	print("EP: " + str(e) + " Score: " + str(score) + "		 ",end="\r", flush=False)

#plt.plot(np.arange(NUM_EPISODES),episode_rewards)
#plt.show()
env.close()
