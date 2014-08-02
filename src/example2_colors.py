# this will load numpy for us
from pylab import *

# load the file and store the result in data
data = np.loadtxt('file.dat')
data2 = np.loadtxt('file2.dat')

# generate a x array of the size of the file
x = np.arange(0, len(data))

# plot
plot(x, data)
plot(x, data2)
savefig('example2_bis.png')
