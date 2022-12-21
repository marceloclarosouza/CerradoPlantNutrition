import pandas as pd
import logging

class DataPreparation():

    def __init__(self, data):
        self.data = data

    def data_subset(self, *args):
        try:
            df = self.data[args]
            return df
            
        except Exception as e:
            msg = f"Error to prepare the subset: {type(e)}, {str(e)}"
            logging.error(msg, exc_info=True)

    def drop_nan(self, axis=None, how=None):
        try:
            df = self.data.dropna(axis=axis, how=how)
            return df

        except Exception as e:
            msg = f"Error to remove NAN: {type(e)}, {str(e)}"
            logging.error(msg, exc_info=True)

    def remove_outlier(self, n_std=3):
        try:
            for col in self.data:
                mean_value = self.data[col].mean()
                sd = self.data[col].std()
                df = self.data[(self.data[col] <= mean_value + (n_std * sd))]
            
            return df
        
        except Exception as e:
            msg = f"Error to remove outlier: {type(e)}, {str(e)}"
            logging.error(msg, exc_info=True)

    def smooth_data(self, alpha=0.5, adjust=True):
        try:
            for col in self.data:
                self.data[col] = self.data[col].ewm(
                    alpha=alpha, adjust=adjust).mean()
            return self.data

        except Exception as e:
            msg = f"Error to smooth data: {type(e)}, {str(e)}"
            logging.error(msg, exc_info=True)

    


