import matplotlib.pyplot as plt
t = [21, 38, 99, 435, 669, 4011]
T = [5.0, 4.0, 3.0, 2.5, 2.4, 2.3]
plt.figure()
plt.scatter(T,t,marker="+")
plt.xlabel("Temperature $T$")
plt.grid(True)
plt.ylabel("Sweeping time $t$")
plt.title("Average of Sweeping Time")
plt.show()
