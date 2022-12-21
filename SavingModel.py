import pickle

class SaveModel():

    def save_model(self, model):
        pickle.dump(model, open("/home/marcelo/Documents/CerradoPlantNutrition/model/model.pkl", "wb"))
