""" Transforming IBGE XLS (awful) tables into something """


import os
import re
import zipfile

import pandas as pd


def retrieve(path):
    for f in os.listdir(path):
        with zipfile.ZipFile(os.path.join(path, f), 'r') as zip_ref:
            zip_ref.extractall(path)


def read_despesas(path, file, cols):
    return pd.read_excel(os.path.join(path, file), header=7, names=cols, encoding='latin-1',
                         skiprows=[61, 62, 63, 64, 65, 66, 67, 68, 69, 70], skipfooter=7, na_values='-')


def read_rendimentos(path, file, cols):
    return pd.read_excel(os.path.join(path, file), sheet_name=4, header=10, names=cols, encoding='latin-1',
                         skipfooter=5, na_values='-', skiprows=[11, 13])


def read_ufs(path):
    output = dict()
    files = os.listdir(path)
    cols = ['name', 'total', 'classe 1', 'classe 2', 'classev3', 'classe 4', 'classe 5', 'classe 6', 'classe 7']
    pattern = r'\d\d'
    ufs = pd.read_csv('ufs_ids.csv', sep=';')
    for file in files:
        if re.match(pattern, file):
            uf = ufs.loc[ufs['nummun'] == int(file[:2]), 'codmun'].iloc[0]
            output[uf] = read_despesas(path, file, cols)
            output[uf] = pd.concat([output[uf], read_rendimentos(path, file, cols)])
    return output


if __name__ == '__main__':
    p = r'originais/'
    # retrieve(p)
    o = read_ufs(p)
    for key in o.keys():
        print(o[key].head(2))
        print(o[key].tail(2))

