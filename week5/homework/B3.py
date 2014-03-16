import math, random
import numpy as np
import matplotlib.pyplot as plt

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

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
                   math.exp(-0.5 * dtau * x[k] ** 2))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x_new ** 2))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    X[step,:] = x
    if step % 10000 == 0:
        print("step %d / %d"%(step,n_steps))

plt.figure()
hist, bin_edges = np.histogram(X.flatten(),density = True, bins = 100)
plt.plot(bin_edges[:-1],hist,"k--",label="numerical value")
x =np.linspace(bin_edges[0],bin_edges[-1],1000) 
y =  np.sqrt(np.tanh(beta/2)) /  np.sqrt(np.pi)* np.exp(- x**2* np.tanh( beta/2))
plt.plot(x,y,label="analyical formula")
plt.title("Normalized Probability Density with the trotter\
        formula\n for $\\beta = 2$ and $N=2^5$ and $n_{steps} = 10^7$\
        and $d\\tau = %.5f"%dtau)
plt.legend()
plt.grid(True)
plt.xlabel("Position $x$")
plt.ylabel("Probability $\pi(x)$")
plt.show()
