# (C2) In order to improve the error estimation for the Markov chain, the "bunching algorithm" does use
# the independent error analysis for the Markov-chain data x_0, x_1, x_2....., x_(n_trials -1), but then
# analyzes these data again, using the independent error analysis, after grouping them into pairs:

# (x_0 + x_1)/2, (x_2 + x_3)/2, (x_4 + x_5)/2, .... (x_(n_trials -2) + x_(n_trials -1))/2

# This process is then repeated for several iterations, making pairs of pairs, then pairs of pairs
# of pairs, etc. This very successful algorithm is implemented for a long sequence of data produced
# by markov_pi.py ( x_i = 4 if it corresponds to a hit, and x_i = 0 otherwise) in the below program,
# that is again provided for convenience. The program produces a plot of error against iteration. 

import random, math
import matplotlib.pyplot as plt

def markov_pi_all_data(N, delta):
    x, y = 1.0, 1.0
    data = []
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x ** 2 + y ** 2 < 1.0:
            data.append(4.0)
        else:
            data.append(0.0)
    return data

poweroftwo = 14
n_trials = 2 ** poweroftwo
delta = 0.1
data = markov_pi_all_data(n_trials, delta)
errors  = []
bunches = []
for i in range(poweroftwo):
    new_data = []
    mean = 0.0
    mean_sq = 0.0
    N = len(data)
    while data != []:
        x = data.pop()
        y = data.pop()
        mean += x + y
        mean_sq += x ** 2 + y ** 2
        new_data.append((x + y) / 2.0 )
    errors.append(math.sqrt(mean_sq / N - (mean / N) ** 2) / math.sqrt(N))
    bunches.append(i)
    data = new_data[:]
plt.figure()
plt.plot(bunches, errors, 'x')
plt.plot(bunches, errors)
plt.grid(True)
plt.xlabel('iteration')
plt.ylabel('naive error')
plt.title('Bunching: naive error vs iteration number')
plt.savefig('apparent_error_bunching.png', format='PNG')
plt.show()

# The observed error is found to increase with the iterations, and exhibits a plateau. 
# This plateau is an excellent estimation of the true error of Markov-chain output. Run this program and answer three questions:

#   Which point on the plot produced by the program of this section corresponds to the naive error of section C1?
#   Why does the error initially increase with the iterations?
#   Why is there a plateau, at all? 
