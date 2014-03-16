import numpy as np
import matplotlib.pyplot as plt, math
import matplotlib.cm as cm

def V(x,cubic,quartic):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot

def Energy(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z(cubic, quartic, beta, n_max):
    Z = np.sum(np.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

def plot_potentials():
    x_max = 5.0
    nx = 100
    dx = 2.0 * x_max / (nx - 1)
    x = np.arange(-(nx - 1) // 2, nx // 2 + 1, dx)

    plt.title('Energy of the different Potentials')
    plt.xlabel('Position x')
    plt.ylabel('Energy')
    plt.plot(x, V(x,0,0), label= "harmonic")
    plt.plot(x, V(x,-0.5,0.5), label= "anharmonic")
    plt.legend(loc=4)
    plt.grid(True)
    plt.axis([-4.0, 4.0, 0.0, 3.0])
    plt.show()

def plot_energy():
    plt.figure()
    plt.title('Energy corrections of different levels')
    plt.xlabel('Value of Quartic = - Cubic ')
    plt.ylabel('Energy')
    quartic = np.linspace(0 ,1,1000) 
    for n in np.arange(0,5,1): 
        plt.plot(quartic, Energy(n,quartic, -quartic),label="n = "+str(n))
    plt.grid(True)
    plt.legend(prop={'size':10},loc= 3)
    plt.show()
def print_app():
    beta = np.linspace(0.1,1,100)
    plt.figure()
    plt.xlabel("beta")
    plt.ylabel("Partition Function")
    for nmax in np.arange(1,30,5):
        plt.plot(beta,Z(0,0,beta,nmax),label="Numerical Value with nmax = "+str(nmax))
    plt.plot(beta,1/(2 *np.sinh(beta/2)), label="Same with sinh")
    plt.legend(loc= 8)
    plt.title("Approximation of the partition function with increasing sum")
    plt.yscale("log")
    plt.show()


print_app()





