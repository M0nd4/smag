import random, math, numpy as np

def direct_disks_box(N, sigma):
    fails = 0.0
    condition = False
    while condition == False:
        L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
        for k in range(1, N):
            a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
            min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) 
            if min_dist < 2.0 * sigma: 
                condition = False
                fails += 1
                break
            else:
                L.append(a)
                condition = True
    return L, (fails/(fails + 1))

N = 4
sigma = 0.1
n_runs = 1000000
failratio_list = []
accept = 0.0
failratio = 0.0
for run in range(n_runs):
    conf, failratio = direct_disks_box(N, sigma)
    failratio_list.append(failratio)
#    print run, conf, ratio
fail_mean = np.mean(failratio_list)
print (1. - fail_mean)
