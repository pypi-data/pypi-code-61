from rest_framework.generics import CreateAPIView
from djangocensus.models.CityModel import CityModel
from djangocensus.rest_api.serializers import CitySerializer


# Create viewset goes here.
class CityCreateViewSet(CreateAPIView):
    serializer_class = CitySerializer
    queryset = CityModel.objects.all()