import math, random, matplotlib.pyplot as plt

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
delta = 1.0
n_steps = 200
x = [2.0] * N
data = []
for step in range(n_steps):
    x = levy_harmonic_path(x[0],x[0],dtau,N)
    x = x[N//2:] + x[:N//2]
    if step%1000:
        print("process \t %.3f "%(step/n_steps*100))
    k = random.randint(0, N - 1)
    for k in x:
        data.append(k)
    

def plot_path():
    plt.figure()
    plt.hist(data, bins=50, normed=True, label='QNC')
    x_values = [0.1 * a for a in range (-30, 30)]
    y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
                      math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]
    plt.plot(x_values, y_values, label='exact')
    plt.xlabel('$x$')
    plt.ylabel('$\\pi(x)$ (normalized)')
    plt.axis([-3.0, 3.0, 0.0, 0.6])
    plt.legend()
    ProgType = 'levy_harm_path'
    plt.title(ProgType + ' beta = ' + str(beta) + ', dtau = ' + str(dtau) + ', Nsteps = '+ str(n_steps))
    plt.show()
plot_path()
