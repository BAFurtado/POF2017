import operator
from collections import OrderedDict

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

import unpacking_reading


def basic_plot_config(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    return ax


def plot_hist(d, decil='total', color='DF', col_num=0):
    fig, ax = plt.subplots()
    ax = basic_plot_config(ax)
    # Sorting data
    data = list(d.keys()), [d[key].loc[col_num][decil] for key in d.keys()]
    x, y = zip(*sorted(zip(data[1], data[0]), reverse=True))
    barlist = ax.bar(y, x)
    barlist[y.index(color)].set_color('r')
    ax.set(xlabel='UFs', ylabel='R$ (2018)', title=o[color].loc[col_num, 'name'] + ' ' + decil)
    ax.tick_params(labelsize=8)
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    d[color].name = d[color].name.str.replace('/', '_')
    fig.savefig('graphs/' + d[color].name.iloc[col_num] + '_' + decil)
    plt.close(fig)


if __name__ == '__main__':
    p = r'originais/'
    o = unpacking_reading.read_ufs(p)
    color_uf = 'DF'
    dec = 'classe 7'
    for i in range(95):
        plot_hist(o, dec, color_uf, i)
