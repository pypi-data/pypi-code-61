from rest_framework.generics import CreateAPIView
from djangocensus.models.DistrictModel import DistrictModel
from djangocensus.rest_api.serializers import DistrictSerializer


# Create viewset goes here.
class DistrictCreateViewSet(CreateAPIView):
    serializer_class = DistrictSerializer
    queryset = DistrictModel.objects.all()