# this will load numpy for us
from pylab import *
data = np.loadtxt('file.dat')
x = np.arange(0, len(data))

#change the limits
xlim(1.5, 3.4)
ylim(-2, 4)

#ticks
xticks([0, 1, 2, 3], ['T0', 'T1', 'T2', 'T3'])
# use np.arange to generate the array of ticks
yticks(np.arange(-2, 4, 0.5))

plot(x, data)
savefig('example2_lims.png')
