from django.apps import AppConfig
from django.conf import settings

import os
import joblib


class CerradoPhysiognomyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cerrado_physiognomy'

class ApiConfig(AppConfig):
    name = 'cerrado_physiognomy'
    MODEL_FILE = os.path.join(settings.MODELS, 'rfc_model.joblib')
    model = joblib.load(MODEL_FILE)
