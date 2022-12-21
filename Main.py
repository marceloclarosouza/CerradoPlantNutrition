import pandas as pd
from DataAquisition import DataAquisition
from DataPreparation import DataPreparation

from Train import model_y_pred

PATH = "/home/marcelo/Documents/CerradoPlantNutrition/cerrado_plants.csv"

def main():
    
    df = DataAquisition(PATH, sep=None, decimal=None)


    subset = list()

    data_subset = DataPreparation(df).data_subset(subset)

    data_drop_nan = DataPreparation(data_subset).drop_nan(axis=0, how=any)

    data_remove_outlier = DataPreparation(data_drop_nan).remove_outlier(n_std=3)

    data_smoothed = DataPreparation(data_remove_outlier).smooth_data(alpha=0.5, adjust=True)


    y_pred = model_y_pred(model, data_split)

    

    

    




if __name__ =="main":
    main()