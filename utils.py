import pandas as pd

def get_scheda(path):
    return pd.read_csv(path, delimiter = ';')