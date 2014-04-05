import random, math
import os
import matplotlib.pyplot as plt

def wave(x):
    return math.exp(-x**2 )/ math.sqrt(math.pi)


def levy_harmonic_path(k, beta):
    xk = tuple([random.gauss(0.0, 1.0 / math.sqrt(2.0 *
                math.tanh(k * beta / 2.0))) for d in range(3)])
    x = [xk]
    for j in range(1, k):
        Upsilon_1 = 1.0 / math.tanh(beta) + 1.0 / \
                          math.tanh((k - j) * beta)
        Upsilon_2 = [x[j - 1][d] / math.sinh(beta) + xk[d] /
                     math.sinh((k - j) * beta) for d in range(3)]
        x_mean = [Upsilon_2[d] / Upsilon_1 for d in range(3)]
        sigma = 1.0 / math.sqrt(Upsilon_1)
        dummy = [random.gauss(x_mean[d], sigma) for d in range(3)]
        x.append(tuple(dummy))
    return x


def rho_harm(x, xp, beta):
    Upsilon_1 = sum((x[d] + xp[d]) ** 2 / 4.0 *
                    math.tanh(beta / 2.0) for d in range(3))
    Upsilon_2 = sum((x[d] - xp[d]) ** 2 / 4.0 /
                    math.tanh(beta / 2.0) for d in range(3))
    return math.exp(- Upsilon_1 - Upsilon_2)

N = 512
T_star = 0.6
beta = 1.0 / (T_star * N ** (1.0 / 3.0))
nsteps = 100000
positions = {}
filename = 'boson_configuration.txt'
positions = {}
# Here we read
if os.path.isfile(filename):
    f = open(filename, 'r')
    for line in f:
        a = line.split()
        positions[tuple([float(a[0]), float(a[1]), float(a[2])])] = \
               tuple([float(a[3]), float(a[4]), float(a[5])])
    f.close()
    if len(positions) != N: exit('we fucked up. its your fault!')
    print( 'starting from file: ', filename)
else:
    for k in range(N):
        a = levy_harmonic_path(1, beta)
        positions[a[0]] = a[0]
    print( 'starting from scratch', filename)

x_data = []
cycle_data = []
cycle_min = 10
perm_cycles = []
for step in range(nsteps):
    boson_a = random.choice(list(positions.keys()))
    perm_cycle = []

    while True:
        perm_cycle.append(boson_a)
        boson_b = positions.pop(boson_a)
        if boson_b == perm_cycle[0]: break
        else: boson_a = boson_b
    k = len(perm_cycle)
    perm_cycles.append(k)
    perm_cycle = levy_harmonic_path(k, beta)
    if k > cycle_min:
        cycle_data.append(perm_cycle[0][0])
    positions[perm_cycle[-1]] = perm_cycle[0]
    for k in range(len(perm_cycle) - 1):
        positions[perm_cycle[k]] = perm_cycle[k + 1]
    a_1 = random.choice(list(positions.keys()))
    b_1 = positions.pop(a_1)
    a_2 = random.choice(list(positions.keys()))
    b_2 = positions.pop(a_2)
    # Metropolis Acceptance Condition
    weight_new = rho_harm(a_1, b_2, beta) * rho_harm(a_2, b_1, beta)
    weight_old = rho_harm(a_1, b_1, beta) * rho_harm(a_2, b_2, beta)
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        positions[a_1] = b_2
        positions[a_2] = b_1
    else:
        positions[a_1] = b_1
        positions[a_2] = b_2
    for particle in positions.keys() : 
        x_data.append((positions[particle])[0])



# Here we write the obtained config, i.e. a dictionnary 
# w/ keys = , values = ,
# into a text file
f = open(filename, 'w')
for a in positions:
   b = positions[a]
   f.write(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + ' ' +  
           str(b[0]) + ' ' + str(b[1]) + ' ' + str(b[2]) + '\n')
f.close()

def hist_data():
    plt.figure()
    plt.hist(x_data, bins = 200, normed = True, alpha = 0.5, label = 'All particle Poitions',range=[-3.,3.])
    plt.hist(cycle_data, bins = 200, normed = True, alpha = 0.5, label = 'Only Particles with cycles more than %d'%cycle_min, range=[-3.,3.])
    dx = 0.01
    x = [i * dx for i in range(-300 , 300)]
    y = [wave(a) for a in x]
    plt.plot(x, y, label = 'analytical wave fct.')
    plt.xlabel('$x$ position')
    plt.ylabel('$\\pi (x)$')
    plt.title('Comparison of the different Distributions of the x-Position')
    plt.legend()
    plt.savefig('Bosons_cycles_histogram.png')
    plt.show()

def hist_perm_cycles():
    plt.figure()
    plt.hist(perm_cycles,bins = 200, normed = True)
    plt.xlabel('$k$ Cycle')
    plt.ylim(0,0.01)
    plt.ylabel('$\\pi (x)$')
    plt.title('Probability of having a $k$ Cycle')
    
    plt.show()




