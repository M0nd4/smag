import random
import math
import matplotlib.pyplot as plt
import os 

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
    return  math.sqrt(d_x**2 + d_y**2)

N = 64
eta = 0.72
sigma = math.sqrt(eta/math.pi/N)
k = int(math.sqrt(N) + 0.5)
# N must be a square Number, otherwise we will not execute
assert math.sqrt(N)%1.0 == 0.0
# Sigma must be smaller than max value where we have dense packing
assert sigma < 1/(2*k) 
L = load_L(k,eta) 
sigma_sq = sigma ** 2
delta = 0.1
n_steps = 10000
u = lambda:random.uniform(-delta, delta)
print("starting now with sigma = %.5f"%sigma)
for steps in range(n_steps):
    a = random.choice(L)
    b = [(a[0] +u() )%1.0, (a[1] + u())%1.0]
    min_dist = min( dist(c,b) for c in L if c != a)
    
    if not (min_dist < 2*sigma ):
        a[:] = b
show_conf(L, sigma, r'$N = %d$ $\eta=%.5f$'%(N,eta), 'inital.png')
