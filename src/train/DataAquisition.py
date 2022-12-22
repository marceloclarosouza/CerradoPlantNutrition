import pandas as pd

class DataAquisition():

    def __init__(self, path, sep=None, decimal=None):
        self.df = pd.read_csv(path, sep=sep, decimal=decimal)
    