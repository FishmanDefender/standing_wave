#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

class Simulation:

    def __init__(self,times):

        self.res = 1000
        self.step = 1

        self.c = np.sqrt(0.5)

        self.pos = [np.zeros(self.res + 2) for _ in range(times + 2)]

        self.pos[0][0] = self.get_sine(0)

        self.pos[1][1] = self.get_sine(0)
        self.pos[1][0] = self.get_sine(1)

        self.square = False

    def square_wave(self):

        for x in range(len(self.pos[0])):

            if x > 0.1*self.res or x < 0.9*self.res:
                self.pos[0][x] = 0.5
                self.pos[1][x] = 0.5

        self.square = True

    def take_step(self):

        for x in range(self.res):
            #print(self.pos[self.step - 1][x+1], self.pos[self.step][x+2], self.pos[self.step][x], self.pos[self.step][x+1])
            self.pos[self.step + 1][x+1] = -self.pos[self.step - 1][x+1]+ pow(self.c,2)*(self.pos[self.step][x+2] + self.pos[self.step][x]) + 2*self.pos[self.step][x+1]*(self.c**2)

        if self.square:
            self.pos[self.step + 1][0] = 0
        else:
            if self.step < self.res/2:
                self.pos[self.step + 1][0] = self.get_sine(self.step + 1) #*np.exp(-(0.005*self.step)**2)
            else:
                self.pos[self.step + 1][0] = 0

        self.pos[self.step + 1][self.res + 1] = 0
        self.pos[self.step + 1][self.res] = 0

        self.step+=1

        #print("END")

    def get_sine(self,num):

        sin_input = 4*np.pi/self.res
        s = 0.5*np.sin(num*sin_input)

        return s

    def get_pos(self):

        return self.pos

cycles = 5000

sim = Simulation(cycles)

if sys.argv[1] == 1:
    sim.square_wave()

for x in range(cycles):
    sim.take_step()

pos = sim.get_pos()

# for x in range(len(pos)):
#     print(pos[x][0],pos[x][1])

fig, ax = plt.subplots()

x = np.arange(0, 1000, 1)
line, = ax.plot(x, np.sin(x))

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(i):
    line.set_ydata(pos[2*i][x])  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=int(cycles/2), interval=1, blit=False, repeat=False)

from matplotlib.animation import FFMpegWriter
writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save("movie.mp4", writer=writer)

plt.show()
