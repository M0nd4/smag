import math
import matplotlib.pyplot as plt
import numpy as np

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
def print_Z():
    print("Z_approx \t Z_int \t Z_ana")
    for quartic in np.arange(0.1,1,0.1):
        cubic = -quartic
        a =  [Z1(beta,cubic,quartic,nmax)]
        a += [Z2(beta,cubic,quartic,x,dx)]
        a += [Z3(beta)]
        if a[0] != np.inf:
            print("quartic: %.5f cubic: %.5f"%(quartic,cubic))
            print("Z_approx: %.5f \t Z_int: %.5f \t Z_ana: %.5f"%(a[0],a[1],a[2]))
def plot_rho():
    quartic = 0.5
    cubic = -0.5
    pi = np.diag(rho_iterated(x,beta,cubic,quartic,dx)) / Z2(beta,cubic,quartic,x,dx)
    plt.figure()
    plt.plot(x, pi,label = "beta = 2")
    plt.grid(True)
    plt.title("Normalized Probability Density with the anharmonic Potential using \n the Trotter formula  and $\\beta=2$, $quartic=0.5$ and $cubic=-0.5$")
    plt.xlabel("Position $x$")
    plt.ylabel("Probability $\pi(x)$")
    plt.show()
plot_rho()
