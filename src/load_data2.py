# glob allows us to list the files that match a pattern
import glob

# pylab will be useful later
from pylab import *

# a simple function to load our files
# we assume that each file has the same number of rows (generations)
def load(dir):
    # example : exp_9/node05_2014-07-15_16_42_48_5178/bestfit.dat
    f_list = glob.glob(dir + '/*/*/bestfit.dat')
    
    # get the number of lines of the first file, to know the size of the matrix
    num_lines = sum(1 for line in open(f_list[0]))
  
    # be careful that np.zeros takes a tuple as argument (size1, size)
    # therefore we need two parentheses
    i = 0;
    data = np.zeros((len(f_list), num_lines)) 

    for f in f_list:
        # we ignore the first column of the file        
        data[i, :] = np.loadtxt(f)[:,1]
        i += 1
    return data

# load our data
data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')
print data_low_mut
