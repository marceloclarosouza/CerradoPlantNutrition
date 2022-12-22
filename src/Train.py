from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report

import pandas as pd

class Model():

    def __init__(self, data):
        self.data = data

    def data_split_train(self, variables, predictor, test_size=0.3, random_state=0):

        X = self.data[variables]
        y = self.data[predictor]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                            random_state=random_state,
                                                            stratify=y)

        data_split = {
            "X_train" : X_train,
            "X_test": X_test,
            "y_train": y_train,
            "y_test": y_test
        }

        return data_split

    def train_random_forest_classification(self, n_estimators=100, n_jobs=-1, random_state=0):
        model = RandomForestClassifier(n_estimators=n_estimators,
                                       random_state=random_state,
                                       n_jobs=n_jobs)
        model.fit(self.data["X_train"], self.data["y_train"])

        return model

    def model_y_pred(self, model):
        y_pred = model.predict(self.data["X_test"])

        return y_pred


    def model_accuracy_score(self, y_pred):
        model_accuracy = metrics.accuracy_score(self.data["y_test"], y_pred)

        return model_accuracy


    def model_feature_score(self, model):
        feature_scores = pd.Series(model.feature_importances_, 
                                   index=self.data["X_train"].columns).sort_values(ascending=False)
        return feature_scores

    def model_classification_report(self, y_pred):
        report = classification_report(self.data["y_test"], y_pred)
        print(report)

        return report

