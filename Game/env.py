import numpy as np
import random
import math


class Snek:

    def __init__(self, size, rewards, food_val, snake_val, food_num, food_decay):
        self.obs_size = size
        self.rewards = rewards
        self.action_size= 4
        self.actions = [0, 1, 2, 3]
        self.cstate = None
        self.snake = None
        self.food = None
        self.food_num = food_num
        self.food_decay = food_decay
        self.head = None
        self.food_val = food_val
        self.snake_val = snake_val
        self.initx = size//2
        self.inity = size//2
        self.len = 1
    
    def reset(self):
        self.food_num *= self.food_decay
        self.snake = []
        self.food = []
        state = np.zeros((self.obs_size, self.obs_size))
        size = self.obs_size
        x = self.initx
        y = self.inity
        for _ in range(math.ceil(self.food_num)):
            foodx = random.randint(0, size - 1)
            foody = random.randint(0, size - 1) 
            state[foodx][foody] = self.food_val
            self.food.append((foodx, foody))
        self.head = (x, y)
        self.snake.append((x, y))
        state[x][y] = self.snake_val
        self.cstate = state
        return state
    
    def step(self, action):
        # Left = 0 Right = 1 Up = 2 Down = 3
        done = False
        food = False
        reward = 0
        dx, dy = 0, 0
        if action == 0:
            dx, dy = -1, 0
        elif action == 1:
            dx, dy = 1, 0
        elif action == 2:
            dx, dy = 0, -1
        elif action == 3:
            dx, dy = 0, 1
        
        
        x, y = self.head
        x += dy
        y += dx
        if x>=self.obs_size or x<0 or y>=self.obs_size or y<0:
            done = True
            print('Reached end')
        
        for i in self.snake[:-1]:
            if i == self.head:
                done = True
                print("ate itself")
        
        s = np.zeros((self.obs_size, self.obs_size))
        
        if not done:
            self.head = (x,y)
            self.snake.append(self.head)

            for p,j in enumerate(self.food):
                if self.head == j:
                    self.len += 1
                    self.food[p] = (random.randint(0, self.obs_size - 1), random.randint(0, self.obs_size - 1))
                    food = True
                    print('Food')

            if self.len < len(self.snake):
                del self.snake[0]
            
            
            for i in self.snake:
                s[i[0]][i[1]] = self.snake_val
            for i in self.food:
                s[i[0]][i[1]] = self.food_val
            self.cstate = s

        if done == True:
            reward = self.rewards['died']
        elif food == True:
            reward = self.rewards['food']
        else:
            reward = self.rewards['live']
        
        return s, reward, done
        