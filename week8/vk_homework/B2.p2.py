import random, math, os

def x_y(k, L):
    y = k // L
    x = k - y * L
    return x, y

for L in [2,4,8,16,32]:
    N = L * L
    nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
                (i // L) * L + (i - 1) % L, (i - L) % N) \
                                        for i in range(N)}
    T = 1
    filename = 'local_'+ str(L) + '_' + str(T) + '.txt'
    if os.path.isfile(filename):
        f = open(filename, 'r')
        S = []
        for line in f:
            S.append(int(line))
        f.close()
        print 'starting from file', filename
    else:
        S = [random.choice([1, -1]) for k in range(N)]
        print( 'starting from scratch')
    nsteps = N * 10
    beta = 1.0 / T
    for step in range(nsteps):
        k = random.randint(0, N - 1)
        delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
        if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
            S[k] *= -1
        if step % 1000 == 0 :
            print("%.3f%%"%(100 * step/nsteps))

    conf = [[0 for x in range(L)] for y in range(L)]
    for k in range(N):
        x, y = x_y(k, L)
        conf[x][y] = S[k]

