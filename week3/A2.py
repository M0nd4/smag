import random
import matplotlib.pyplot as plt
import math

def show_conf(L, sigma, title, fname):
    plt.figure()
    plt.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = plt.Circle((x + ix, y + iy), radius = sigma,  fc = 'r')
                plt.gca().add_patch(cir)
    plt.axis('scaled')
    plt.title(title)
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.xlabel("x Position")
    plt.ylabel("y Position")
    plt.savefig(fname)
    plt.show()


def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)
L = [[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]]
sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.1
n_steps = 1000

u = lambda:random.uniform(-delta, delta)
for steps in range(n_steps):
    a = random.choice(L)
    b = [(a[0] +u() )%1.0, (a[1] + u())%1.0]
    min_dist = min( dist(c,b) for c in L if c != a)
    if not (min_dist < 2*sigma ):
        a[:] = b
print(L)
show_conf(L, sigma, 'Markov disks with periodic boundary', 'B1.png')
