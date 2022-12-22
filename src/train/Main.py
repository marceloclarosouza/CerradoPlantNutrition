
from DataAquisition import DataAquisition
from DataPreparation import DataPreparation
from Train import Model
from GraphicalAnalysis import GraphicalAnalysis
from SavingModel import SaveModel

import pandas as pd
import os

def main():
    path = os.path.normpath("/home/marcelo/Documents/CerradoPlantNutrition/sample/cerrado_physiognomies.csv")
    
    #data aquisition
    data_aq = DataAquisition(path, sep=",", decimal=".")
    df = pd.DataFrame(data_aq.df)

    
    #data preparation
    subset = ["N(g kg-1)","P(g kg-1)","K(g kg-1)","Ca(g kg-1)","Mg(g kg-1)","Fe(mg kg-1)","Mn(mg kg-1)","Vegetation"]

    data_subset = DataPreparation(df).data_subset(subset)

    data_drop_nan = DataPreparation(data_subset).drop_nan(axis=0, how="any")

    data_remove_outlier = DataPreparation(data_drop_nan).remove_outlier(subset, n_std=3)

    data_smoothed = DataPreparation(data_remove_outlier).smooth_data(subset, alpha=0.5, adjust=True)



    #spliting data
    split_data = Model(data_smoothed).data_split_train(subset[:-1], subset[-1],
                                                         test_size=0.3, random_state=0)
    
    
    #training model
    train_model = Model(split_data).train_random_forest_classification(n_jobs=-1, random_state=0)

    
    #scores    
    y_pred = Model(split_data).model_y_pred(train_model)

    model_accuracy = Model(split_data).model_accuracy_score(y_pred)

    print(model_accuracy)

    feature_score = Model(split_data).model_feature_score(train_model)

    print(feature_score)

    classification_report = Model(split_data).model_classification_report(y_pred)

    print(classification_report)
    

    ##Graphical analysis
    GraphicalAnalysis().feature_barplot(feature_score)

    conf_matrix = GraphicalAnalysis().feature_confusion_matrix(y_pred, split_data)

    GraphicalAnalysis().feature_heatmap(conf_matrix)

    
    #saving the model
    SaveModel().save_model(train_model)

if __name__ == "__main__":
    main()