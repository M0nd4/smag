import math, random, pylab

# free density matrix calculation
def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x

beta = 20.0
N = 80
dtau = beta / N
delta = 1.7
n_steps = 100000
x = [2.0] * N
data = []
acc = 0 # for the acceptance rate
for step in range(n_steps):

    x = levy_harmonic_path(x[0], x[0], beta / N, N)
    x = x[(N / 2):] + x[:(N / 2)]

#    k = random.randint(0, N - 1)
#    knext, kprev = (k + 1) % N, (k - 1) % N
#    x_new = x[k] + random.uniform(-delta, delta)

    # weighting calculation as in lecture
#    old_weight  = (rho_free(x[knext], x[k], dtau) *
#                   rho_free(x[k], x[kprev], dtau) *
#                   math.exp(-0.5 * dtau * x[k] ** 2))
#    new_weight  = (rho_free(x[knext], x_new, dtau) *
#                   rho_free(x_new, x[kprev], dtau) *
#                   math.exp(-0.5 * dtau * x_new ** 2))
#    if random.uniform(0.0, 1.0) < new_weight / old_weight:
#        x[k] = x_new
#        acc += 1
    if step % 1 == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])
pylab.hist(data, bins=50, normed=True, label='QMC')
x_values = [0.1 * a for a in range (-30, 30)]
y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
                  math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]

print(float(acc) / n_steps)

pylab.plot(x_values, y_values, label='exact')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 0.6])
pylab.legend()
ProgType = 'levy_harm_path'
pylab.title(ProgType + ' beta = ' + str(beta) + ', dtau = ' + str(dtau) + ', Nsteps = '+ str(n_steps))
pylab.savefig(ProgType + str(beta) + '.png')
pylab.show()
