import glob
from pylab import *

def load(dir):
    f_list = glob.glob(dir + '/*/*/bestfit.dat')
    num_lines = sum(1 for line in open(f_list[0]))
    i = 0;
    data = np.zeros((len(f_list), num_lines)) 
    for f in f_list:
        data[i, :] = np.loadtxt(f)[:,1]
        i += 1
    return data

# compute the median of each column
def med(data):
    median = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
    return median

data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')

# generate the x
n_generations = data_low_mut.shape[1]
x = np.arange(0, n_generations)

# compute the medians
med_low_mut = med(data_low_mut)
med_high_mut = med(data_high_mut)

plot(x, med_low_mut)
plot(x, med_high_mut)

savefig('medians1.png')
