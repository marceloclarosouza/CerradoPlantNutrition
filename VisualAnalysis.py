from sklearn.metrics import confusion_matrix

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class VisualAnalysis():

    def feature_barplot(self, feature_score):
        sns.barplot(x=feature_score, y=feature_score.index)
        plt.xlabel("Feature Importance Score")
        plt.ylabel("Feature")
        plt.show()

    def feature_confusion_matrix(self, y_pred, **data):
        cm = confusion_matrix(data["y_test"], y_pred, normalize=True)
        np.set_printoptions(precision=2)
        return cm

    def feature_heatmap(self, cm):
        sns.heatmap(cm, annot=True, fmt=".2f", cmap="YlGnBu")
        plt.show()

    

