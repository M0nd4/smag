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
def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x
cubic = -1
quartic = 1
def V(y):
    return y**2 / 2 + cubic * y**3 + quartic * y**4
beta = 20.0
N = 80
dtau = beta / N
delta = 1.0
n_steps = 30000
x0 = 0
x = [x0] * N
Ncut = 58
#Choosing appropriate initial values
w = lambda y: math.exp(sum(-a **2/ 2.0 * dtau for a in y))
w2 = lambda y: math.exp(sum(-V(a) *  dtau for a in y))
data = []
Weight_old = w(x)
for step in range(n_steps):
    x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    Weight_new = w(x_new) 
    if random.random() < min(1, Weight_new/ Weight_old):
        Weight_old = Weight_new
        x = x_new[:]
    random.shuffle(x)
    if step%1000==0:
        print("process \t %.3f "%(step/n_steps*100))
    for k in x:
        data.append(k)
print(len(data))    
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
    ProgType = 'levy_harm_path_metropolis'
    plt.title(ProgType + ' beta = ' + str(beta) + ', dtau = ' + str(dtau) + ', Nsteps = '+ str(n_steps))
    plt.show()
plot_path()
