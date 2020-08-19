import pygame
import time
import numpy as np
import random


class snek:

    def __init__(self, size):
        self.size = size
        self.rewards = None
        self.action_space_size = 4
        self.actions = [0, 1, 2, 3]
        self.cstate = None
        self.dis = None
    
    def reset(self):
        state = np.zeros((self.size, self.size))
        size = self.size
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        foodx = random.randint(0, size - 1)
        foody = random.randint(0, size - 1) 
        state[x][y] = 2
        state[foodx][foody] = -1
        self.cstate = state
        return state

    def start_render(self):
        pygame.init()
        self.dis = pygame.display.set_mode((self.size *10, self.size *10))
        pygame.display.update()

    def step(action):
        pass


    def render_state(self, state):
        height = 10
        width = 10
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 2:
                    pygame.draw.rect(self.dis, (0, 0, 255), [j*10, i*10, height, width])
                elif state[i][j] == -1:
                    pygame.draw.rect(self.dis, (255, 0, 0), [j*10, i*10, height, width])
        


    def stop_render(self):
        pygame.quit()
        quit()

snake = snek(64)
state = snake.reset()
snake.start_render()
print('Started Render')
for i in range(10):
    snake.render_state(state)
    pygame.display.update()
time.sleep(5)
snake.stop_render()


