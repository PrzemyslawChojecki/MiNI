"""
Losowanie punktow w R^n
Aby policzyc pole w n-tym wymiarze
"""

import math
import random

def distance(x, y):
    suma = 0
    for i in range(len(x)):
        suma += (x[i] - y[i])**2
    return math.sqrt(suma)

assert (distance([1], [1]) == 0)

def random_point(n, a=-1, b=1):
    x = [None] * n
    for i in range(n):
        x[i] = random.uniform(a, b)
    return(x)

def volume_exact(n, r=1):
    return ( (r**n)*( (math.pi)**(n/2) )) / math.gamma(n/2+1)

def unit_ball_ratio(n):
    return (volume_exact(n)/(2**n))

def volume_approx(n, m=10000):
    punkt = [None] * n
    ilosc_trafien = 0
    for i in range(m):
        if distance(random_point(n), [0] * n) < 1:
            ilosc_trafien += 1
    return((ilosc_trafien/m)*2**n)


import matplotlib.pyplot as plt

fig = plt.figure()

y_exact = [None] * 19
y_approx = [None] * 19
y_ratio = [None] * 19

x = range(1, 20)
for i in range(18):
    y_exact[i] = volume_exact(i+1)
    y_approx[i] = volume_approx(i+1)
    y_ratio[i] = unit_ball_ratio(i+1)

ax1 = fig.add_subplot(2, 1, 1)
ax1.scatter(x, y_approx, color="red", marker=(3,0,0))
ax1.scatter(x, y_exact)
ax1.grid()

ax2 = fig.add_subplot(2, 1, 2)
ax2.scatter(x, y_ratio)
ax2.grid()

fig.savefig('volume.png', dpi=90)














