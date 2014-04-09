import random, math, os
import numpy as np

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

L = 6
N = L * L
T = 2.0
filename = 'local_'+ str(L) + '_' + str(T) + '.txt'
nsteps = N * 3000000
beta = 1.0 / T
E_means=[]
for runs in range(4):

    nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
    S = [random.choice([1, -1]) for k in range(N)]
    Energy = energy(S, N, nbr)
    E = 0
    for step in range(nsteps):
        k = random.randint(0, N - 1)
        delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
        if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
            S[k] *= -1
            Energy += delta_E
        E += Energy
        if step%5000 == 0:
            print("%.3f%%"%(100*step/nsteps))
    E_mean = E/ nsteps / N
    print( E_mean, 'mean energy')
    E_means += [E_mean]
print(E_means)
print(np.mean(E_means))
