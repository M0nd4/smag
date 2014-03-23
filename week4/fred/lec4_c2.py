import random
import matplotlib.pyplot as plt

def q_mean(d, n_trials):
    x = [0]*d
    r2 = 0
    Q = 0
    for i in range(n_trials):
        k = random.randint(0, d - 1)
        x_new_k = x[k] + random.uniform(-1.0, 1.0)
        r2_new = r2 - x[k]**2 + x_new_k**2  
        if r2_new < 1:
            x[k] = x_new_k
            r2 = r2_new
        x_supp = random.uniform(-1.0,1.0)
        if r2 + x_supp**2 < 1:
            Q += 1
    Q_mean = Q / float(n_trials)
    return Q_mean

dmax = 200
n_trials = 1000000
Vol1_s = [0.0,2.0]      #added an arbitrary dimension 0, to assign Vol1_s(d) to Vol1_s[d]
dim = [0,1]
for d in range(2,dmax+1):
    dim.append(d)
    Q_mean = q_mean(d - 1, n_trials)
    Vol1_s_d = 2 * Q_mean * Vol1_s[d - 1]
    Vol1_s.append(Vol1_s_d)
    if d == 5: print('Vol1_s(d=%i) = %f' % (d, Vol1_s[d]))
    if d == dmax: print('Vol1_s(d=%i) = %f' % (d, Vol1_s[d]))

plt.figure()
plt.semilogy(dim, Vol1_s)
plt.title('markov_Vol1_s_accordion: Vol1_s as a function of dimension $d$\n%i trials for each $d$'%n_trials)
plt.xlabel('$d$')
plt.ylabel('Vol1_s($d$)')
plt.savefig('lec4_c2_markov_Vol1_s_accordion.png')
plt.show()
plt.clf()

