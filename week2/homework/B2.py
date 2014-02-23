import numpy as np
V = 0.8 ** 2
N = 4
p_accept = 0.51516 
Z = V * p_accept
Q = (0.2)**2
P1 = Q**N * 24
P2 = (Q/Z)**N * 24
print("sigma = 0: %.5f and with sigma = 0.1: %.5f "%(P1,P2))
