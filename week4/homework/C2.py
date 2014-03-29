import random
import numpy as np
from scipy.special import gamma

def Vol1_s(d):
    return np.pi ** (d/ 2.0)/ gamma(d/ 2.0 + 1.0)


def markov(d,dmax):
    n_trials = 1000000

    x = [0] * d
    mean = ls = n_hits = Q = 0
    
    for n in range(n_trials):
        k = random.randint(0,d-1)
        a = random.uniform(-1.0,1.0)
        x_supp = random.uniform(-1.0,1.0)
        s = ls + 2 * a * x[k] + a**2
        if s < 1:
            x[k] += a
            n_hits += 1
            ls = s
        if ls+x_supp**2 < 1:
            Q += 1
   
        mean += ls
            
        if n%10000==0:
            print("%d / %d %.5f%%"%(d,dmax,100*(d+n/n_trials)/dmax))
    return (2 * Q/n_trials)
dmax = 200
vv = [Vol1_s(1)]
for d in range(1,dmax+1): 
    vv += [vv[d-1]*markov(d,dmax)]
plt.figure()
plt.plot(vv)
plt.yscale("log")
plt.title("Markov Chain Calculation of the Volume of the d-dimensional Sphere")
plt.xlabel("Dimension d")
plt.ylabel("Volume")
plt.show()

