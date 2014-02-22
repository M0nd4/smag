import numpy as np
import random
import matplotlib.pyplot as plt
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.1197
sigma_sq = sigma ** 2
delta = 0.1
n_steps = 2000000
histo_data = np.zeros([n_steps,4,2]) 
for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist < 4.0 * sigma ** 2):
        a[:] = b
    histo_data[steps,:,:] = np.array(L)
    if steps%10000==0:
        print("%.5f%%"%(steps/n_steps*100))
def hist_data():
    plt.figure()
    plt.hist((histo_data[:,:,0].flatten()), bins=100, normed=True)
    plt.xlabel(r'Position $x$')
    plt.ylabel(r'frequency')
    plt.title("Histogram of the x-Position with Markov sampling")
    plt.grid()
    plt.show()
hist_data()
