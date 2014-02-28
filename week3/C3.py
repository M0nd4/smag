import random
import math
import matplotlib.pyplot as plt
import os 
import cmath
import numpy as np
def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y


def Psi_6(L, sigma_sq,N):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 **2 * sigma_sq and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0: vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)

def load_L(k,eta):
    N = k**2
    filename = 'discs_%d_%.5f.txt'%(N,eta)
    if os.path.isfile(filename):
        f = open(filename, 'r')
        L = []
        for line in f:
            a, b = line.split()
            L.append([float(a), float(b)])
        f.close()
        print( 'starting from file', filename)
    else:
        L = []
        for k1 in range(k):
            for k2 in range(k):
                L.append([k1/k, k2/k])
        print( 'starting from scratch')
    f = open(filename, 'w')
    for a in L:
       f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
    f.close()
    return L
    
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
    return  d_x**2 + d_y**2

N = 64
etas = np.arange(0.72,0.60,-0.001)
k = int(math.sqrt(N) + 0.5)
# N must be a square Number, otherwise we will not execute
assert math.sqrt(N)%1.0 == 0.0
L = load_L(k,0.72) 
delta = 0.1
n_steps = 10000
u = lambda:random.uniform(-delta, delta)
psis= []
etas_ = []
for eta in etas: 
    sigma = math.sqrt(eta/math.pi/N)
    sigma_sq = sigma ** 2
    print("starting now with eta = %.5f"%eta)
    for steps in range(n_steps):
        a = random.choice(L)
        b = [(a[0] +u() )%1.0, (a[1] + u())%1.0]
        min_dist = min( dist(c,b) for c in L if c != a)
        
        if not (min_dist < 4*sigma_sq ):
            a[:] = b
        if steps%100==0:
            psis.append(abs(Psi_6(L,sigma_sq,N)))
            etas_.append(eta)
    eta -= 0.01
def plot_psi():
    plt.figure()
    plt.scatter(etas_,psis)
    plt.xlabel(r"Density $\eta$")
    plt.ylabel(r"$\psi_6$")
    plt.title("Phase transition in the Psi Funktion")
    plt.show()
plot_psi()
#show_conf(L, sigma, r'$N = %d$ $\eta=%.5f$'%(N,eta), 'inital.png')
