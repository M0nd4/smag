import random, math, os
 
def direct_Vol1_s(N, d):
    n_hits = 0
    for i in range(N):
        sum_x_sqr = 0
        for j in range(d):
            x_j = random.uniform(-1.0,1.0)
            sum_x_sqr += x_j**2
            if sum_x_sqr > 1.0:
                break
            if j == d-1:
                n_hits += 1
    return n_hits

def Vol1_cube(dimension):
    return 2**dimension

def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)



n_trials = 1000000
dim_max = 12
hit_condition = True
d = 1
filename = 'lec4_b1_table_Vol1_for_d.txt'
f = open(filename, 'w')
head = '----------------------------------------------------------\n' + \
'%i trials used for all d\n'%n_trials  + \
'd  | estimation of Vol1_s(d) | Vol1_s(d) (exact) |  n_hits\n' + \
'----------------------------------------------------------\n'
f.write(head)
while hit_condition:
    n_hits = direct_Vol1_s(n_trials, d)
    ratio = n_hits / float(n_trials)
    Vol1_s_est = ratio * Vol1_cube(d)
    Vol1_s_exact = Vol1_s(d)
    d_str = str(d)
    if d < 10: d_str = ' ' + d_str
    i_str = (len(str(n_trials)) - len(str(n_hits)))*' ' + str(n_hits)
    f.write(d_str + ' |                %f |          %f | ' % (Vol1_s_est, Vol1_s_exact) + i_str +'\n')
    d += 1
    if 0 == n_hits: hit_condition = False
f.close()
