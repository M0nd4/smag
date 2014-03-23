import random
import numpy as np
from scipy.special import gamma

def Vol1_s(d):
    return np.pi ** (d/ 2.0)/ gamma(d/ 2.0 + 1.0)


def markov(d,N,N_max,n_trials):

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
            
    return (2 * Q/n_trials)

N_runs = 20
means = []
meansq = []
std   = []
print("n_trials | <Vol1_s(20)> |  Error  | Vol1_s(20) (exact result) |")
for t in range(5+1):
    n_trials = 10**t
    d_20= np.array([markov(20,N,N_runs,n_trials) for N in range(N_runs)])
    d_20 *= Vol1_s(19)
    means += [np.mean(d_20)]
    meansq += [np.mean(d_20**2)]
    std += [np.std(d_20)]
    print("%d\t|%.5f\t|%.5f\t|%.5f\t|"%(n_trials,means[-1],std[-1],Vol1_s(20)))
