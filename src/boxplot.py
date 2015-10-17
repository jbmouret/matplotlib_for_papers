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

data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')
low_mut_100 = data_low_mut[:, 100]
high_mut_100 =  data_high_mut[:, 100]

fig = figure()
ax = fig.add_subplot(111)

bp = ax.boxplot([low_mut_100, high_mut_100], notch=0, sym='b+', vert=1, whis=1.5, 
             positions=None, widths=0.6)

savefig('boxplot1.png')
