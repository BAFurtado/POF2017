import plotting
import unpacking_reading


def main(path, decil, color):
    dic = unpacking_reading.read_ufs(path)
    # Gráficos de despesa 95
    for i in range(95):
        plotting.plot_hist(dic, decil, color, i)


if __name__ == '__main__':
    # Path to originals
    p = r'originais/'
    # Choose classes 'total', 'classe 1', 'classe 2', 'classev3', 'classe 4', 'classe 5', 'classe 6', 'classe 7'
    dec = 'classe 7'
    # UF to color
    uf_to_color = 'DF'
    main(p, dec, uf_to_color)
