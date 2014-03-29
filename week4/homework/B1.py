from random import uniform as u
import numpy as np
from scipy.special import gamma
def direct_Vol1_s(N,d):
    n_hits = 0
    for i in range(N):
        sum_x_sqr = 0
        for j in range(d):
            x_j = u(-1.0,1.0)
            sum_x_sqr += x_j**2
            if sum_x_sqr > 1.0:
                break;
        else:
            n_hits += 1
    return n_hits
def Vol1_cube(d):
    return 2**d

def Vol1_s(d):
    return np.pi ** (d/ 2.0)/ gamma(d/ 2.0 + 1.0)


n_trials = int(10E5)
d_max = 12
no_hits = False
d = 1
print("""--------------------------------------------------------
1000000 n_trials used for all
d\t | Vol1_s(d) (estimate)\t | Vol1_s(d) (exact)\t | n_hits \t
--------------------------------------------------------""")
while not no_hits:
    n_hits = direct_Vol1_s(n_trials,d)
    no_hits = not n_hits
    Vol1_s_est = n_hits / n_trials *Vol1_cube(d)
    Vol1_s_exact = Vol1_s(d) 
    print("%d\t | %.5f\t\t | %.5f\t\t | %d\t"%(d, Vol1_s_est,Vol1_s_exact,n_hits))
    d += 1

     


            

