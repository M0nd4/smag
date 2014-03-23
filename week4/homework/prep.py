# Using python3.3
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

def Vol1_s(d):
    return np.pi ** (d/ 2.0)/ gamma(d/ 2.0 + 1)

d = np.linspace(1,200+1,100)
plt.figure()
plt.plot(d,Vol1_s(d))
plt.yscale("log")
plt.xlabel("Dimension $d$")
plt.title("Volume of the $d$-Dimensional Unit Hypersphere") 
plt.ylabel("Volume")
plt.grid(True)
plt.show()

print(Vol1_s(5))
print(Vol1_s(20))
print(Vol1_s(200))
