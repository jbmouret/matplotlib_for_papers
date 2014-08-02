# glob allows us to list the files that match a pattern
import glob

# pylab will be useful later
from pylab import *

# a simple function to load our files
def load(dir):
    # example : exp_9/node05_2014-07-15_16_42_48_5178/bestfit.dat
    f_list = glob.glob(dir + '/*/*/bestfit.dat')
    d = []
    for f in f_list:
        d += [np.loadtxt(f)]
    return d

# load our data
data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')

print data_low_mut
print data_high_mut
