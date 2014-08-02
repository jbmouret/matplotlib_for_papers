# Pylab includes numpy as 'np'
from pylab import *

# create an array of 256 points (x), from -pi to +pi
x = np.linspace(-np.pi, np.pi, 256)

# compute cos(x) [thanks to numpy, cos(x) returns an array]
y = np.cos(x)

# compute the plot
plot(x, y)

# Show it in a new window
show()
