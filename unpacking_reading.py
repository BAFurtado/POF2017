import zipfile
import os
import re
import pandas as pd


def retrieve(path):
    for f in os.listdir(path):
        with zipfile.ZipFile(os.path.join(path, f), 'r') as zip_ref:
            zip_ref.extractall(path)


def read_ufs(path):
    output = dict()
    files = os.listdir(path)
    cols = ['name', 'tot', 1, 2, 3, 4, 5, 6, 7]
    pattern = r'\d\d'
    for i in files:
        if re.match(pattern, i):
            output[i[:2]] = pd.read_excel(os.path.join(p, i), header=7, names=cols,
                              skiprows=[61, 62, 63, 64, 65, 66, 67, 68, 69, 70], skipfooter=7, na_values='-')
    return output


if __name__ == '__main__':
    p = r'\\storage6\usuarios\# BERNARDO ALVES FURTADO #\POF2017\Originais'
    # retrieve(p)
    o = read_ufs(p)
    for key in o.keys():
        print(o[key].head(2))
