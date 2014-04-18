import pylab

x = [5., 4., 3., 2.5, 2.4, 2.3]
y = [22, 31, 87, 505, 1194, 3915]

l2 = [0, 4000]

pylab.plot(x, y, label = 'correlation time function')
pylab.plot([2.27, 2.27], l2, label = 'critical temperature')
pylab.xlabel('temperature')
pylab.ylabel('correlation sweeping time')
pylab.legend()
pylab.savefig('correlation_time_explosion.png')
pylab.show()
