import gym
import numpy as np
#import matplotlib.pyplot as plt
import copy
#https://github.com/stephencwelch/Neural-Networks-Demystified/blob/master/Part%204%20Backpropagation.ipynb

import numpy as np
class Neural_Network(object):
    def __init__(self):
        #Define Hyperparameters
        self.inputLayerSize = 4
        self.outputLayerSize = 2
        self.hiddenLayerSize = 3

        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)

    def forward(self, X):
        #Propogate inputs though network
        #print(X.shape)
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.soft(self.z3)
        return yHat

    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))

    def sigmoidPrime(self,z):
        #Gradient of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)

    def soft(self,x):
        shiftx = x - np.max(x)
        #np.clip(shiftx,-10,10)
        exps = np.exp(shiftx)
        return exps / np.sum(exps)

    def softprime(self,x,row):
        s = x.reshape(-1,1)
        jacobian = (np.diagflat(s) - np.dot(s, s.T))
        returnrow=jacobian[row,:]
        returnrow=np.reshape(returnrow,(1,-1))
        return returnrow




    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)

        delta3 = np.multiply((y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)


        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)


        return dJdW1, dJdW2
    def addW1(self,x):
        self.W1+=x
    def addW2(self,x):
        self.W2+=x



#Hyperparameters
NUM_EPISODES = 10000
LEARNING_RATE = 0.000025
GAMMA = 0.99

# Create gym and seed numpy
env = gym.make('CartPole-v0')
nA = env.action_space.n
#print(nA)
#np.random.seed(1)

# Init weight
#w = np.random.rand(4, 2)

# Keep stats for final print of graph
episode_rewards = []
nn=Neural_Network()
# Our policy that maps state to action parameterized by w


# Vectorized softmax Jacobian

# Main loop
# Make sure you update your weights AFTER each episode
for e in range(NUM_EPISODES):

	state = env.reset()[None,:]

	grads1 = []
	grads2 = []
	rewards = []

	# Keep track of game score to print
	score = 0

	while True:

		# Uncomment to see your model train in real time (slower)
		#env.render()

		# Sample from policy and take action in environment
		#print(state)
		#2d array of 4 values
		#print(state)

		probs = nn.forward(state)
		#print(probs)
		#2d array of 2 values
		#print(probs)
		#print(nA)
		#na=2
		#print(probs[0])
		#print(probs)
		#1d array of 2 values
		#(2)
		#first value in probs is prob of zero, second is prob of one
		#action=0
		#print(probs)
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
		actionarray=np.zeros((2))
		actionarray[action]=1
		#state=np.reshape(4,1)
		#print(state.shape)
		d1softmax,d2softmax = nn.costFunctionPrime(state, actionarray)
		#print(dsoftmax.size)
		#gradients in the column of the actions
		#there are as many columns as actions
		#print(dsoftmax)
		d1log = d1softmax / probs[0,action]
		d2log = d2softmax / probs[0,action]
		#print(dlog.size)
		grad1 = d1log
		grad2 = d2log
		#print(grad.size)
		#print("State")
		#print(state)
		#print(state.T)
		#grads1.append(grad1)
		#grads2.append(grad2)
		grads1.append(d1softmax)
		grads2.append(d2softmax)
		rewards.append(reward)

		score+=reward

		# Dont forget to update your old state to the new state
		state = next_state

		if done:
			break

	# Weight update
	for i in range(len(grads2)):

		# Loop through everything that happend in the episode and update towards the log policy gradient times **FUTURE** reward
		#sum is v(t)
		 nn.addW1(LEARNING_RATE * grads1[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])]))
		 nn.addW2(LEARNING_RATE * grads2[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])]))
		#print(LEARNING_RATE * grads[i] * sum([ r * (GAMMA ** r) for t,r in enumerate(rewards[i:])]))

	# Append for logging and print
	episode_rewards.append(score)
	print("EP: " + str(e) + " Score: " + str(score) + "         ",end="\r", flush=False)

#plt.plot(np.arange(NUM_EPISODES),episode_rewards)
#plt.show()
env.close()
