import math
import matplotlib.pyplot as plt
import numpy as np
import random
# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))
def V(x,cubic,quartic):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot

def Energy(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)


def Z1(beta,cubic, quartic, n_max):
    Z = np.sum(np.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z
def Z2(beta,cubic,quartic,grid,dx):
    return np.sum(np.diag(rho_iterated(grid,beta,cubic,quartic,dx)))*dx
def Z3(beta):
    return 1/(2* math.sinh(beta/2)) 
def monte_carlo(beta,cubic,quartic):
    beta = 2.0
    N = 2 **5
    dtau = beta / N
    delta = 1.0
    n_steps = int(10**7)
    X = np.zeros([n_steps,N])
    x = [0.0] * N
    for step in range(n_steps):
        k = random.randint(0, N - 1)
        knext, kprev = (k + 1) % N, (k - 1) % N
        x_new = x[k] + random.uniform(-delta, delta)
        old_weight  = (rho_free(x[knext], x[k], dtau) *
                       rho_free(x[k], x[kprev], dtau) *
                       math.exp(- dtau * V(x[k],cubic,quartic)))
        new_weight  = (rho_free(x[knext], x_new, dtau) *
                       rho_free(x_new, x[kprev], dtau) *
                       math.exp(- dtau * V(x_new,cubic,quartic)))
        if random.uniform(0.0, 1.0) < new_weight / old_weight:
            x[k] = x_new
        X[step,:] = x
        if step % 10000 == 0:
            print("step %d / %d"%(step,n_steps))
    return X




# unharmonic density matrix in the Trotter approximation (returns the full matrix)
def rho_trotter(grid, beta,cubic,quartic):
    return np.array([[rho_free(x, xp, beta) * np.exp(- 0.5 * beta *  (V(xp,cubic,quartic)+ V(x,cubic,quartic))) for x in grid] for xp in grid])
def rho_iterated(grid,beta,cubic,quartic,dx):
    beta_tmp = 2.0 ** (-5)                   # initial value of beta (power of 2)
    rho = rho_trotter(x, beta_tmp,cubic,quartic)  # density matrix at initial beta
    while beta_tmp < beta:
        rho = np.dot(rho, rho)
        rho *= dx
        beta_tmp *= 2.0
    return rho

x_max = 5.0                              # the x range is [-x_max,+x_max]
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) // 2, nx // 2 + 1)] 
beta     = 2 
cubic = 0
quartic = 0
nmax = 100

def compare():
    quartic = 0.5
    cubic = -0.5
    pi = np.diag(rho_iterated(x,beta,cubic,quartic,dx)) / Z2(beta,cubic,quartic,x,dx)
    pi2, bin_edges = np.histogram(monte_carlo(beta,cubic,quartic),density = True,normed=True, bins = 100)
    plt.figure()
    plt.plot(x, pi,label = "Matrix Squaring Method")
    plt.plot(bin_edges[:-1],pi2,"k--",label="Montecarlo Sampling Method")
    plt.grid(True)
    plt.title("Normalized Probability Density: Comparison of Matrix Squaring with Monte Carlo Sampling with $\\beta=2$, $quartic=0.5$ and $cubic=-0.5$")
    plt.xlabel("Position $x$")
    plt.ylabel("Probability $\pi(x)$")
    plt.legend()
    plt.show()
compare()
