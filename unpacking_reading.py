""" Transforming IBGE XLS (awful) tables into something """


import os
import re
import zipfile

import pandas as pd


def retrieve(path):
    for f in os.listdir(path):
        with zipfile.ZipFile(os.path.join(path, f), 'r') as zip_ref:
            zip_ref.extractall(path)

#
# def state_string(state, states_codes):
#     state_id = states_codes.loc[states_codes['codmun'] == state]['nummun']
#     return str(state_id.iloc[0])


def read_ufs(path):
    output = dict()
    files = os.listdir(path)
    cols = ['name', 'tot', 1, 2, 3, 4, 5, 6, 7]
    pattern = r'\d\d'
    ufs = pd.read_csv('ufs_ids.csv', sep=';')
    for i in files:
        if re.match(pattern, i):
            uf = ufs.loc[ufs['nummun'] == int(i[:2]), 'codmun'].iloc[0]
            output[uf] = pd.read_excel(os.path.join(path, i), header=7, names=cols,
                              skiprows=[61, 62, 63, 64, 65, 66, 67, 68, 69, 70], skipfooter=7, na_values='-')
    return output


if __name__ == '__main__':
    p = r'\\storage6\usuarios\# BERNARDO ALVES FURTADO #\POF2017\Originais'
    # retrieve(p)
    o = read_ufs(p)
    for key in o.keys():
        print(o[key].head(2))
