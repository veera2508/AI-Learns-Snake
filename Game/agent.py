from dqnet import DQN
import random
import numpy as np


class agent:
    def __init__(self, env, batch_size, epsilon = 1, epsilon_decay = 0.99, discount_factor = 0.9, net_input = (64, 64, 2), no_of_actions = 4, ermax = 50000):
        self.env = env
        self.batch_size = batch_size
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.dqn = DQN(net_input, no_of_actions)
        self.er = []
        self.ermax = ermax
        self.discount_factor = discount_factor

    def epsilon_policy(self, state, test = False):
        '''
        Function which finds the action probabilities based on epsilon policy given a specific state

        Input:
        state - The current state of the environment

        Returns:
        Probabilities of all the actions
        ''' 
        q = self.dqn.predict(state)

        if random.random() <= self.epsilon and not test:
            return random.randrange(self.env.action_space)
        else:
            return np.argmax(q)
    
    def add_exp(self, state, action, reward, next_state, done):
        self.er.append({'state':state,
                        'action':action,
                        'reward':reward,
                        'next_state':next_state,
                        'done': done})
        if len(self.er) > self.ermax:
            self.er.pop(0)
    
    def update_network(self):
        '''
        Function which updates the network to the target q values
        '''
        samples = random.sample(self.er, self.batch_size)
        hist = self.dqn.update_network(samples, self.discount_factor)
        return round(hist.history['loss'][0], 3)
    
    def prepopulate_er(self):
        '''
        Function to prepopulate the experience replay by batch size
        '''
        state = self.env.reset()
        i = 0
        while i < self.batch_size:
            j = 0
            action = self.epsilon_policy(state)
            avg_reward = 0
            states = []
            states.append(state)
            while j < 2:
                if j == 1:
                    action = self.epsilon_policy(np.stack(states))
                next_state, reward, done = self.env.step(action)
                avg_reward += reward
                j+=1
                if done:
                    state = self.env.reset()
                    states.append(state)
                    break
                else:
                    state = next_state
                    states.append(state)
            
            while(len(states)!= 3):
                states.append(states[-1])

            stack = np.stack(states[:-1], axis = -1)
            next_stack = np.stack(states[1:], axis = -1)
            self.add_exp(stack, action, reward, next_stack, done)
            i+=1
    

    
        