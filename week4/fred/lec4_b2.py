import random
import matplotlib.pyplot as plt

d = 2
n_trials = 1000000

x = [0]*d
norm_sqr = 0
sum_norm_sqr = 0
for i in range(n_trials):
    k = random.randint(0, d - 1)
    x_new_k = x[k] + random.uniform(-1.0, 1.0)
    norm_sqr_new = norm_sqr - x[k]**2 + x_new_k**2  
    if norm_sqr_new < 1:
        x[k] = x_new_k
        norm_sqr = norm_sqr_new
    sum_norm_sqr += norm_sqr
r2_mean = sum_norm_sqr / float(n_trials)
print('for d = %i,  n_trails = %i: r^2_mean = %f' %(d,n_trials,r2_mean))
