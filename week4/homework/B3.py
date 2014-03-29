import random
def markov(d):
    n_trials = 1000000

    x = [0] * d
    mean = ls = n_hits = Q = 0
    
    for n in range(n_trials):
        k = random.randint(0,d-1)
        a = random.uniform(-1.0,1.0)
        x_supp = random.uniform(-1.0,1.0)
        s = sum(x[i]**2 for i in range(d)) + 2 * a * x[k] + a**2
        if s < 1:
            x[k] += a
            n_hits += 1
            ls = s
        if ls+x_supp**2 < 1:
            Q += 1
   
        mean += ls
            
        if n%10000==0:
            print("%.5f%%"%(100*n/n_trials))
    print(2 * Q/n_trials)
markov(1)
