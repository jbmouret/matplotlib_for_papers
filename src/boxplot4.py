import glob
from pylab import *

# import colors
from palettable.colorbrewer.qualitative import Set2_7
colors = Set2_7.mpl_colors

params = {
    'axes.labelsize': 8,
    'font.size': 8,
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
    i = 0
    data = np.zeros((len(f_list), num_lines))
    for f in f_list:
        data[i, :] = np.loadtxt(f)[:, 1]
        i += 1
    return data


data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')
low_mut_100 = data_low_mut[:, 100]
high_mut_100 = data_high_mut[:, 100]

fig = figure()
ax = fig.add_subplot(111)

bp = ax.boxplot([low_mut_100, high_mut_100], notch=0, sym='b+', vert=1, whis=1.5,
                positions=None, widths=0.6)


for i in range(len(bp['boxes'])):
    box = bp['boxes'][i]
    box.set_linewidth(0)
    boxX = []
    boxY = []
    for j in range(5):
        boxX.append(box.get_xdata()[j])
        boxY.append(box.get_ydata()[j])
        boxCoords = list(zip(boxX, boxY))
        boxPolygon = Polygon(boxCoords, facecolor=colors[i % len(colors)], linewidth=0)
        ax.add_patch(boxPolygon)

for i in range(0, len(bp['boxes'])):
    bp['boxes'][i].set_color(colors[i])
    # we have two whiskers!
    bp['whiskers'][i*2].set_color(colors[i])
    bp['whiskers'][i*2 + 1].set_color(colors[i])
    bp['whiskers'][i*2].set_linewidth(2)
    bp['whiskers'][i*2 + 1].set_linewidth(2)
    # fliers
    bp['fliers'][i].set(markerfacecolor=colors[i],
                        marker='o', alpha=0.75, markersize=6,
                        markeredgecolor='none')
    bp['medians'][i].set_color('black')
    bp['medians'][i].set_linewidth(3)
    # and 4 caps to remove
    for c in bp['caps']:
        c.set_linewidth(0)


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.tick_params(axis='x', direction='out')
ax.tick_params(axis='y', length=0)

ax.grid(axis='y', color="0.9", linestyle='-', linewidth=1)
ax.set_axisbelow(True)

ax.set_xticklabels(['low\nmutation', 'high\nmutation'])

fig.subplots_adjust(left=0.2)


savefig('boxplot4.png')
