import os
import pandas as pd
from train.DataAquisition import DataAquisition
from train.DataPreparation import DataPreparation
from model_execution.ExecuteModel import ExecuteModel


def main():
    path = os.path.normpath("/home/marcelo/Documents/CerradoPlantNutrition/sample/cerrado_physiognomies.csv")
    
    #data aquisition
    data_aq = DataAquisition(path, sep=",", decimal=".")
    df = pd.DataFrame(data_aq.df)

    
    #data preparation
    subset = ["N(g kg-1)","P(g kg-1)","K(g kg-1)","Ca(g kg-1)","Mg(g kg-1)","Fe(mg kg-1)","Mn(mg kg-1)"]

    data_subset = DataPreparation(df).data_subset(subset)

    data_drop_nan = DataPreparation(data_subset).drop_nan(axis=0, how="any")

    data_remove_outlier = DataPreparation(data_drop_nan).remove_outlier(subset, n_std=3)

    data_smoothed = DataPreparation(data_remove_outlier).smooth_data(subset, alpha=0.5, adjust=True)

    read_model = ExecuteModel(data_smoothed).load_model()

    print(read_model)

if __name__ == "__main__":
    main()



