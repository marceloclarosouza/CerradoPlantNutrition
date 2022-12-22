import pickle
import logging

class ExecuteModel():
    def __init__(self, data):
        self.data = data
    
    def load_model(self):
        try:
            open_model = pickle.load(open("/home/marcelo/Documents/CerradoPlantNutrition/model/model.pkl", "rb"))
            result = open_model.predict(self.data)
            return result
            
        except Exception as e:
            msg = f"Error to load the model: {type(e)}, {str(e)}"
            logging.error(msg, exc_info=True)
