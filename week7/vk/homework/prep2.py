import random
import matplotlib.pyplot as plt

data = []
for run in range(100000):
    data.append(random.uniform(0.0, 1.0))
plt.figure()
plt.title('Preparation program 2, SMAC week 7, 2014')
plt.hist(data, bins=200, range=[0.5, 0.6], normed=True)
plt.xlabel('$x$')
plt.ylabel('$\\pi(x)$')
plt.show()
