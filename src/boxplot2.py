import glob
from pylab import *

params = {
    'axes.labelsize': 8,
    'text.fontsize': 8,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': False,
    'figure.figsize': [2.5, 4.5]
}
rcParams.update(params)

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

# now all plot function should be applied to ax
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.tick_params(axis='x', direction='out')
ax.tick_params(axis='y', length=0)

ax.grid(axis='y', color="0.9", linestyle='-', linewidth=1)
ax.set_axisbelow(True)


savefig('boxplot2.png')
