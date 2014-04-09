import random, math

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

L = 6
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N)
                                    for i in range(N)}
T = 2.0
p  = 1.0 - math.exp(-2.0 / T)
nsteps = 1000000
S = [random.choice([1, -1]) for k in range(N)]
E = [energy(S, N, nbr)]
for step in xrange(nsteps):
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
        print "\t %.8f%%"%(step/(nsteps/100.0))
print sum(E)/ len(E) / N
