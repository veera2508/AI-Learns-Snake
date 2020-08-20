import pyglet
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
        self.snake = None
        self.food = None
        self.scolor = (0, 0, 255)
        self.fcolor = (255, 0, 0)
    
    def reset(self):
        self.snake = []
        state = np.zeros((self.size, self.size))
        size = self.size
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        foodx = random.randint(0, size - 1)
        foody = random.randint(0, size - 1) 
        self.food = (foodx, foody)
        self.snake.append((x, y))
        self.cstate = state
        return state

    def start_render(self):
        self.dis = pyglet.window.Window(self.size *10, self.size *10)

    def render(self):
        dis = self.dis
        batch = pyglet.graphics.Batch()
        squares = []
        for i in self.snake:
            squares.append(pyglet.shapes.Rectangle(i[1] * 10, (self.size - i[0] - 1) * 10, 10, 10, color = self.scolor, batch = batch))
        squares.append(pyglet.shapes.Rectangle(self.food[1] * 10, (self.size - self.food[0]) * 10, 10, 10, color = self.fcolor, batch = batch))
        
        @dis.event
        def on_draw():
            dis.clear()
            batch.draw()
        
        @dis.event
        def update(self):
            dis.clear()
            batch.draw()
        
        self.dis.


    def step(self, action):
        pass

env = snek(64)
env.start_render()
for i in range(20):
    state = env.reset()
    env.render()
    print('Done')


        





