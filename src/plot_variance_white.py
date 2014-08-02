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

def perc(data):
    median = np.zeros(data.shape[1])
    perc_25 = np.zeros(data.shape[1])
    perc_75 = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
        perc_25[i] = np.percentile(data[:, i], 25)
        perc_75[i] = np.percentile(data[:, i], 75)
    return median, perc_25, perc_75

data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')

# generate the x
n_generations = data_low_mut.shape[1]
x = np.arange(0, n_generations)

# compute the medians and 25/75 percentiles
med_low_mut, perc_25_low_mut, perc_75_low_mut = perc(data_low_mut)
med_high_mut, perc_25_high_mut, perc_75_high_mut = perc(data_high_mut)

axes(frameon=0, axisbelow=True)
tick_params(axis='x', top='off')
tick_params(axis='y', right='off')
tick_params(axis='y', left='off')


grid(axis='y', color="0.9", linestyle='-', linewidth=1)
#grid(axis='y')

fill_between(x, perc_25_low_mut, perc_75_low_mut, alpha=0.25, linewidth=0, color='#B22400') 
fill_between(x, perc_25_high_mut, perc_75_high_mut, alpha=0.25, linewidth=0, color='#006BB2')


plot(x, med_low_mut, linewidth=2, color='#B22400')
plot(x, med_high_mut, linewidth=2, linestyle='--', color='#006BB2')

xlim(-5, 400)
ylim(-5000, 300)

xticks(np.arange(0, 500, 100))


legend = legend(["Low mutation rate", "High Mutation rate"], loc=4);
frame = legend.get_frame()
#frame.set_facecolor('0.9')
#frame.set_edgecolor('0.9')
frame.set_facecolor('1.0')
frame.set_edgecolor('1.0')

savefig('variance_white.png')
