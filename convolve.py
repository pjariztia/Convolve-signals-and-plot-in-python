# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:03:12 2019

@author: Pariztial
"""

import numpy as np
from numpy import linspace, cos, sin, exp, convolve, abs, where
import matplotlib.pyplot as plt

n = 100
t = np.linspace(-8, 8, n)
T = t[1] - t[0]  # sampling width

#typical functions
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
def step(x):
    return where(x>=0, 1, 0)
def ramp(x):
    return x*where(x>=0, 1, 0)
def rect(x):
    return where(abs(x)<=0.5, 1, 0)
def sinc(x):
    return (sin(np.pi*x))/(np.pi*x)
def trian(x):
    return np.maximum(0, 1-abs(t))

#enter your function x1 and x2 to convolve and plot
x1 = np.maximum(0, 3-abs(t)) -np.maximum(0, 2-abs(3*t))
x2 = np.where(np.logical_and(t>=-2, t<=2), 1, 0)

y = np.convolve(x1, x2, mode='full') * T #for scale convolve
ty = np.linspace(2*-8, 2*8, n*2-1)
 
fg, ax = plt.subplots(1, 1)
ax.plot(t, x1, label="$x_1$")
ax.plot(t, x2, label="$x_2$")
ax.plot(ty, y, label="$x_1\\star x_2$")
plt.axis([-8, 8, -1, 7])
ax.legend(loc='best')
ax.grid(True)

fg.canvas.draw()