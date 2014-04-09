conf = [[0 for x in range(L)] for y in range(L)]
for k in xrange(N):
        x, y = x_y(k, L)
        conf[x][y] = S[k]

