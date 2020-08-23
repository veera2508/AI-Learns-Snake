import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.models import Sequential

class DQN:
    def __init__(self, input_shape, no_of_actions):
        self.model = Sequential([
        Conv2D(32, kernel_size = (2,2), input_shape = input_shape, activation = tf.nn.relu, kernel_initializer = "he_uniform"),
        MaxPooling2D((2,2)),
        Conv2D(64, kernel_size = (2,2), activation = tf.nn.relu, kernel_initializer = "he_uniform"),
        MaxPooling2D((2,2)),
        Conv2D(64, kernel_size = (3,3), activation = tf.nn.relu, kernel_initializer = "he_uniform"),
        MaxPooling2D((2,2)),
        Flatten(),
        Dropout(0.1),
        Dense(512, activation = tf.nn.relu, kernel_initializer = "he_uniform"),
        Dense(no_of_actions, activation = "linear", kernel_initializer = "he_uniform")
        ])
        self.model.compile(optimizer = Adam(0.005), loss = 'mean_squared_error')

    def predict(self, state):
        state = np.expand_dims(state, axis = 0)
        return self.model.predict(state)
    
    def update_network(self, samples, discount_factor):
        States = np.array([s[0] for s in samples])
        Next_States = np.array([s[3] for s in samples])
        target = self.model.predict(States, batch_size = len(samples))
        target_next = self.model.predict(Next_States, batch_size = len(samples))

        for j,s in enumerate(samples):
            state, action, reward, next_state, done = s
            if done:
                target[j][action] = reward
            else:
                target[j][action] = reward + (discount_factor * np.max(target_next[j]))
        
        hist = self.model.fit(States, target, batch_size = len(samples), verbose = False)
        return hist
    
    def save(self, filename = None):
        f = ('model.h5' if filename is None else filename)
        self.model.save_weights('Game/models' + f)
    
    def load(self, path):
        self.model.load_weights(path)
    

    

