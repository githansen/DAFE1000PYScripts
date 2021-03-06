import math
import numpy as np


def eulers(funksjon, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0, len(t) - 1):
        y[n + 1] = y[n] + f(y[n], t[n]) * (t[n + 1] - t[n])
        print(y[n])
    return y


t = np.linspace(1, 2, 21)
f = lambda x,y: x/y
eulers(f,1,t)