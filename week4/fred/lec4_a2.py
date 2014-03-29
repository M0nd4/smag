import random, math
import matplotlib.pyplot as plt

def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

x = []
y = []
for dimension in range(1,200):
    x.append(dimension)
    y.append(Vol1_s(dimension))

plt.figure()
plt.semilogy(x,y)
plt.title('hypersphere volume: Vol1_s(d) over d for integer dimensions')
plt.xlabel('d')
plt.ylabel('Vol1_s(d)')
plt.savefig('lec4_a2_exact_Vol1_s.png')
plt.show()
plt.clf()

#Compute volume for d = {5, 20, 200}:
d_vals = [5, 20, 200]
for d in d_vals:
    print('d = %i,  \tVol1_s(%i) = %e' % (d, d, Vol1_s(d)))

#Calculate Vol1_s(200) / Vol1_s(199) (for exercise C1)
print()
print('Vol1_s(200) / Vol1_s(199) = %f'%(Vol1_s(200) / Vol1_s(199)))
