#!/usr/bin/env python3
import numpy as np

class Simulation:

    def __init__(self):

        self.res = 100

        self.pos0 = np.zeros(self.res + 2)
        self.pos1 = np.zeros(self.res + 2)

        self.pos0[0] = get_sine(0)

        self.pos1[1] = get_sine(0)
        self.pos1[0] = get_sine(1)

    def step(self):

        

    def get_sine(self,num):

        sin_input = 2*np.pi/self.res
        s = np.sin(num*sin_input)

        return s
