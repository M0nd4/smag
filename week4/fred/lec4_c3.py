import random, os, math
import matplotlib.pyplot as plt

def Vol1_s_exact(dimension):
        return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

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

def Vol1_s_d(dmax, n_trials):
    Vol_old = 2.0
    for d in range(2,dmax+1):
        Q_mean = q_mean(d - 1, n_trials)
        Vol = 2 * Q_mean * Vol_old
        Vol_old = Vol
    return Vol

d = 20
max_pow = 5
n_runs = 20
Vol_exact = Vol1_s_exact(d)

filename = 'lec4_c3_error_estimation.txt'
f = open(filename, 'w')
n_length = max( 8 , (max_pow + 1) ) 
head1 = ' Vol1_s(20) (exact result) = %f' %Vol_exact + '\n'
delta = 'abs(<Vol1_s(20)> - Vol1_s(20))'
head2 = 'n_trials' + max(n_length - 8, 0)*' ' + ' | <Vol1_s(20)> |  Error   | ' + delta + ' |\n'
head3 = len(head2)*'-' + '\n'
head = head1 + head2 + head3
f.write(head)

n_trials = []
mean_Vol = []
mean_sqr_Vol = []
error = []
for pow in range(max_pow + 1):
    n_trials.append(10**pow)
    sum_Vol = 0
    sum_sqr_Vol = 0
    for run in range(n_runs):
        print(n_trials, run)
        Vol_n = Vol1_s_d(d, n_trials[pow])
        sum_Vol += Vol_n
        sum_sqr_Vol += Vol_n**2
    mean_Vol.append(sum_Vol / float(n_runs))
    mean_sqr_Vol.append(sum_sqr_Vol / float(n_runs))
    error.append(math.sqrt( (mean_sqr_Vol[-1] - mean_Vol[-1] ** 2)  / float(n_runs) ))
    
    n_str = (n_length - pow - 1)*' ' + str(n_trials[-1]) 
    line = n_str + ' |     %f | %f | '% (mean_Vol[-1], error[-1]) + (len(delta) -8 )*' ' + '%f |\n' % (abs(mean_Vol[-1] - Vol_exact))
    f.write(line)

f.close()
