import math
import numpy as np
import matplotlib.pyplot as plt

def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def rho_harmonic_trotter(grid, beta):
    return np.array([[rho_free(x, xp, beta) * \
                         np.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])

x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) // 2, nx // 2 + 1)]
beta = 8
beta_tmp = beta / 2**5
rho = rho_harmonic_trotter(x, beta_tmp)
while beta_tmp < beta:
    rho = np.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
Z1 = np.sum(np.diag(rho))*dx
Z2 = 1/(2* math.sinh(beta/2)) 
plt.figure()
plt.plot(x, np.diag(rho)/Z1,label = "numerical values")
x = np.array(x)
y = (np.sqrt(np.tanh (beta/2))) / np.sqrt(np.pi) * np.exp(- x**2 *  np.tanh(beta/2))
plt.title(r"Normalized Probability Density with the trotter formula for $\beta = 8$")
plt.grid(True)
plt.xlabel("Position $x$")
plt.ylabel("Probability $\pi(x)$")
plt.plot(x,y,label="analytical formula")
plt.legend()
plt.show()
