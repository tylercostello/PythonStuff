import gym

import agent

SAVE_FREQUENCY = 10
env = gym.make('CartPole-v1')
state = env.reset()
score = 0
episode = 0
prev_frame = None
state_size = 4
action_size = env.action_space.n
g = agent.LinearSoftmaxAgent(state_size, action_size)


MAX_EPISODES = 100000
while episode < MAX_EPISODES:  # episode loop
    # env.render()
    action, prob = g.act(state)
    state, reward, done, info = env.step(action)  # take a random action
    if done:
        reward = -10
    score += reward
    g.store(state, action, prob, reward)

    if done:
        episode += 1
        g.train()
        if (episode%100==0):
            print('Episode: {} Score: {}'.format(episode, score))
        score = 0
        state = env.reset()
        if episode % SAVE_FREQUENCY == 0:
            g.save()
