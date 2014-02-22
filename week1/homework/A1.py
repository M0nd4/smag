import random, math, matplotlib.pyplot as plt
import random, math, pylab

def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits

n_runs = 500
n_trials_list = []
sigmas = []
for poweroftwo in range(4, 13):
    n_trials = 2 ** poweroftwo
    sigma = 0.0
    for run in range(n_runs):
        pi_est = 4.0 * direct_pi(n_trials) / float(n_trials)
        sigma += (pi_est - math.pi) ** 2
    sigmas.append(math.sqrt(sigma/(n_runs)))
    n_trials_list.append(n_trials)

plt.figure()
plt.plot(n_trials_list, sigmas, 'x')
import numpy as np
p = np.polyfit(np.log(n_trials_list),np.log(sigmas),1)
plt.plot(n_trials_list, np.exp(np.polyval(p,np.log(n_trials_list))))
plt.annotate(r'$\alpha = %.5f$'%p[0], xy=(.5, .6), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=16) 
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.xlabel('Number of trials')
plt.ylabel('$\sigma$')
plt.grid(True)
plt.title('Direct sampling: Standard deviation $\sigma$ as a function of n_trials')
#plt.savefig('direct_sampling_statistical_error.png')
plt.show()
