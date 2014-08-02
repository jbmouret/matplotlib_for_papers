import glob
from pylab import *
import brewer2mpl

 # brewer2mpl.get_map args: set name  set type  number of colors
bmap = brewer2mpl.get_map('Set2', 'qualitative', 7)
colors = bmap.mpl_colors
 
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



def plot_data(ax, min_gen, max_gen):
    # now all plot function should be applied to ax
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.tick_params(axis='x', direction='out')
    ax.tick_params(axis='y', length=0)
    # offset the spines
    for spine in ax.spines.values():
            spine.set_position(('outward', 5))
    ax.grid(axis='y', color="0.9", linestyle='-', linewidth=1)
    # put the grid behind
    ax.set_axisbelow(True)

    ax.fill_between(x, perc_25_low_mut, perc_75_low_mut, alpha=0.25, linewidth=0, color=colors[0]) 
    ax.fill_between(x, perc_25_high_mut, perc_75_high_mut, alpha=0.25, linewidth=0, color=colors[1])


    ax.plot(x, med_low_mut, linewidth=2, color=colors[0])
    ax.plot(x, med_high_mut, linewidth=2, linestyle='--', color=colors[1])

    # change xlim to set_xlim
    ax.set_xlim(min_gen, max_gen)
    ax.set_ylim(-5000, 300)

    #change xticks to set_xticks
    ax.set_xticks(np.arange(min_gen, max_gen, 100))

    legend = ax.legend(["Low mutation rate", "High Mutation rate"], loc=4);
    frame = legend.get_frame()
    frame.set_facecolor('1.0')
    frame.set_edgecolor('1.0')


data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')

n_generations = data_low_mut.shape[1]
x = np.arange(0, n_generations)

med_low_mut, perc_25_low_mut, perc_75_low_mut = perc(data_low_mut)
med_high_mut, perc_25_high_mut, perc_75_high_mut = perc(data_high_mut)

fig = figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
plot_data(ax1, 0, 500)
plot_data(ax2, 0, 110)

fig.savefig('variance_subplot_bis.png')
