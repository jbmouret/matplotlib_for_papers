import glob
from pylab import *


params = {
    'axes.labelsize': 8,
    'text.fontsize': 8,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': False,
    'figure.figsize': [4.5, 4.5]
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

axes(frameon=0)
grid()

plot(x, med_low_mut, linewidth=2, color='#B22400')
plot(x, med_high_mut, linewidth=2, linestyle='--', color='#006BB2')

xlim(-5, 400)
ylim(-5000, 300)

xticks(np.arange(0, 500, 100))

legend = legend(["Low mutation rate", "High Mutation rate"], loc=4);
frame = legend.get_frame()
frame.set_facecolor('0.9')
frame.set_edgecolor('0.9')

savefig('medians3.png')
