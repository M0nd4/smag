import matplotlib.pyplot as plt
import random
import numpy as np
def markov_plot():
    n_trials = 100000
    d = 2

    x = [0] * d
    xl = [x]
    n_hits = 0
    for n in range(n_trials):
        k = random.randint(0,d-1)
        a = random.uniform(-1.0,1.0)
        s = sum(x[i]**2 for i in range(d)) + 2 * a * x[k] + a**2
        if s < 1:
            x[k] += a
            n_hits += 1
        xl += [x[:]]
        if n%10000==0:
            print("%.5f%%"%(100*n/n_trials))
    xl = np.array(xl)
    plt.figure()
    plt.scatter(xl[:,0],xl[:,1])
    plt.show()
def markov():
    n_trials = 1000000
    d = 2

    x = [0] * d
    mean = ls = n_hits = 0
    
    for n in range(n_trials):
        k = random.randint(0,d-1)
        a = random.uniform(-1.0,1.0)
        s = sum(x[i]**2 for i in range(d)) + 2 * a * x[k] + a**2
        if s < 1:
            x[k] += a
            n_hits += 1
            ls = s
            
        mean += ls
            
        if n%10000==0:
            print("%.5f%%"%(100*n/n_trials))
    print(mean/n_trials)

