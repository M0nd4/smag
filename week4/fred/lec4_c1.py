import random
import matplotlib.pyplot as plt

def q_mean(d, n_trials):
    x = [0]*d
    r2 = 0
    Q = 0
    for i in range(n_trials):
        k = random.randint(0, d - 1)
        x_new_k = x[k] + random.uniform(-1.0, 1.0)
        r2_new = r2 - x[k]**2 + x_new_k**2  
        if r2_new < 1:
            x[k] = x_new_k
            r2 = r2_new
        x_supp = random.uniform(-1.0,1.0)
        if r2 + x_supp**2 < 1:
            Q += 1
    Q_mean = Q / float(n_trials)
    return Q_mean

d = 199
n_trials = 1000000

print('for %i trials:'%n_trials)
print('d = %i'%d)
Q_mean = q_mean(d, n_trials)
print('Vol1_s(%i) / Vol1_s(%i) = %f'%(d+1,d,2*Q_mean))
