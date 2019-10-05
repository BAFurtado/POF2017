import plotting
import unpacking_reading


def main(d):
    # Gráficos de despesa 95
    for i in range(95):
        plotting.plot_hist(d, i)


if __name__ == '__main__':
    p = r'originais/'
    o = unpacking_reading.read_ufs(p)
    main(o)
