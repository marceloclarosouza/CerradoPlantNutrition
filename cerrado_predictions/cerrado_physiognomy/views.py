from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response

class RfcPrediction(APIView):
    def post(self, request):
        data = request.data
        N = data["N"]
        P = data["P"]
        K = data["K"]
        Ca = data["Ca"]
        Mg = data["Mg"]
        Fe = data["Fe"]
        Mn = data["Mn"]

        rand_frt_class = ApiConfig.model
        cerrado_physiognomy = rand_frt_class.predict([[N, P, K, Ca, Mg, Fe, Mn]])
        
        response_dict = {"Predicted Physiognomy": cerrado_physiognomy}
        return Response(response_dict, status=200)