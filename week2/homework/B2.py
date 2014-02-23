import numpy as np
V = 0.8 ** 2
N = 4
p_accept = 0.51516 
Z = V * p_accept
Q = (0.2)**2
P = (Q/Z)**N * 24
print(P)
