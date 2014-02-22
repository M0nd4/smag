import random, math

def direct_disks_box(N, sigma):
    condition = False
    fails = 0  
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
    return L, fails

N = 4
sigma = 0.1
n_runs = 1000000
conf_a = [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75,0.75)]
conf_b = [(0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75)]
conf_c = [(0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70)]
hits = 0
Total = 0
del_xy = 0.1
configuration = conf_c
all_fails, success = 0,0
for run in range(n_runs):
    x_vec, fails = direct_disks_box(N, sigma)
    all_fails += fails
    success += 1
    cond = True
    for b in configuration: 
        cond_b = min( max( abs(a[0] - b[0]), abs(a[1] - b[1]) ) for a in x_vec)  < del_xy
        cond *= cond_b
    if cond: hits += 1

    if run%10000==0:
        print("%.3f%%"%(run/n_runs*100))
print( '%.5f proportion of confs in eight-dimensional volume element.'%(hits / float(n_runs)))
print( '%.5f acceptance rate'%(success / all_fails))
