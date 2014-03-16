import math
import matplotlib.pyplot as plt

n_states = 4
grid_x = [i * 0.2 for i in range(-25, 26)]
dx = 0.2
En =[n+0.5 for n in range(n_states)]
psi = {}
for x in grid_x:
    psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]  # ground state
    psi[x].append(math.sqrt(2.0) * x * psi[x][0])         # first excited state
    # other excited states (through recursion):
    for n in range(2, n_states):
        psi[x].append(math.sqrt(2.0 / n) * x * psi[x][n - 1] -
                      math.sqrt((n - 1.0) / n) * psi[x][n - 2])
def rho(x,x_,beta):
    return sum( math.exp(- En[n]*beta ) * psi[x][n]*psi[x_][n] for n in range(n_states))
def Z1(beta):
    return sum(math.exp(-beta * En[n]) for n in range(n_states))
def Z2(beta):
    return sum(rho(x,x,beta) for x in grid_x)*dx
def Z3(beta):
    return 1/(2* math.sinh(beta/2)) 
print(Z1(2))
print(Z2(2))
print(Z3(2))
beta = 2
plt.figure()
plt.plot(grid_x, [rho(x,x,beta)/Z2(beta) for x in grid_x],label = "beta = 2")
plt.legend()
plt.title("Normalized Probability Density")
plt.xlabel("Position x")
plt.ylabel("Probability")
plt.show()
