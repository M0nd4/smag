import random, math, os
import matplotlib.pyplot as plt
def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E


def x_y(k, L):
    y = k // L
    x = k - y * L
    return x, y
CV = []
for L in [2,4,8,16,32]:
    T = 2.27
    N = L * L
    nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
                (i // L) * L + (i - 1) % L, (i - L) % N) \
                                        for i in range(N)}
    filename = 'local_'+ str(L) + '_' + str(T) + '.txt'
    if os.path.isfile(filename):
        f = open(filename, 'r')
        S = []
        for line in f:
            S.append(int(line))
        f.close()
        print( 'starting from file', filename)
    else:
        S = [random.choice([1, -1]) for k in range(N)]
        print( 'starting from scratch')
    p  = 1.0 - math.exp(-2.0 / T)
    nsteps = 100
    S = [random.choice([1, -1]) for k in range(N)]
    E = [energy(S, N, nbr)]
    for step in range(nsteps):
        k = random.randint(0, N - 1)
        Pocket, Cluster = [k], [k]
        while Pocket != []:
            j = Pocket.pop()
            for l in nbr[j]:
                if S[l] == S[j] and l not in Cluster \
                       and random.uniform(0.0, 1.0) < p:
                    Pocket.append(l)
                    Cluster.append(l)
        for j in Cluster:
            S[j] *= -1
        E.append(energy(S, N, nbr))
        if step%10000 == 0:
            print( "L = %d \t %.8f%%"%(L,step/(nsteps/100.0)))

    E_mean = sum(E)/ len(E)
    E2_mean = sum(a ** 2 for a in E) / len(E)
    cv = (E2_mean - E_mean ** 2 ) / N / T ** 2
    CV += [cv]
    
    f = open(filename, 'w')
    for a in S:
       f.write(str(a) + '\n')
    f.close()
