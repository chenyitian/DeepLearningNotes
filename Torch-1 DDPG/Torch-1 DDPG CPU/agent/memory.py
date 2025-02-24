"""
@author: Young
@license: (C) Copyright 2013-2017
@contact: aidabloc@163.com
@file: memory.py
@time: 2018/1/16 21:33
"""
from collections import namedtuple, deque
import random
import numpy as np

experience = namedtuple("Experience",
                        ["state", "action", "reward", "done", "next_state"])


class Memory(object):
    def __init__(self, max_size=int(1e6)):
        self.cache = deque(maxlen=max_size)
        self.max_size = max_size
        self.length = 0

    def __len__(self):
        if self.length >= self.max_size:
            return self.max_size
        else:
            return self.length

    def __call__(self, *args, **kwargs):
        return self.append(*args)

    def append(self, state, action, reward, done, next_state):
        self.length += 1
        self.cache.append(experience(
            state, action, reward, done, next_state))

    def sample(self, batch_size=64):
        batch_size = min(batch_size, self.length)
        batch = random.sample(self.cache, batch_size)

        states = np.float32([i.state for i in batch])
        actions = np.float32([i.action for i in batch])
        rewards = np.float32([i.reward for i in batch])
        next_states = np.float32([i.next_state for i in batch])
        return states, actions, rewards, next_states




