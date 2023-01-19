from django.urls import path
from .views import RfcPrediction

urlpatterns = [
    path('rfcprediction/', RfcPrediction.as_view(), name='rfcprediction'),
]

