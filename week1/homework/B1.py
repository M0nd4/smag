import random
import numpy as np
import matplotlib.pyplot as plt

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    accepts = 0 
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            accepts += 1
        if x**2 + y**2 < 1.0: 
            n_hits += 1
    return n_hits,accepts

n_runs = 500
n_trials = 1000
dels = np.arange(0.1,5.0 + 0.1, 0.1)
acc = np.zeros(len(dels))

def acc():
    for d in range(len(dels)):
        for run in range(n_runs):
                acc[d] += markov_pi(n_trials, dels[d])[1] / n_trials
        acc[d]/= n_runs
        print("%.3f "%(100*d/len(dels)))
    plt.figure()
    plt.plot(dels,acc)
    plt.xlabel(r"Rejected factor $\delta$")
    plt.ylabel(r"Acceptance ratio")
    plt.title(r"$\frac{1}{2}$ Rule of Thumb")
    plt.grid(True)
    plt.show()
def plot_rms():
    sigmas= []
    for d in range(len(dels)):
        sigma = 0.0
        for run in range(n_runs):
            pi_est = 4.0*markov_pi(n_trials, dels[d])[0] / n_trials
            sigma += (pi_est - np.pi) ** 2
        sigmas+=[np.sqrt(sigma/n_runs)]
        print("%.3f "%(100*d/len(dels)))
    plt.figure()
    plt.plot(dels,sigmas)
    plt.xlabel(r"Rejected factor $\delta$")
    plt.ylabel(r"rms error")
    plt.title(r"$\frac{1}{2}$ Rule of Thumb")
    plt.grid(True)
    plt.show()

plot_rms()
