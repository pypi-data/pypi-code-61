from rest_framework.generics import CreateAPIView
from djangocensus.models.ReligiousPopulationModel import ReligiousPopulationModel
from djangocensus.rest_api.serializers import ReligiousPopulationSerializer


# Create viewset goes here.
class ReligiousPopulationCreateViewSet(CreateAPIView):
    serializer_class = ReligiousPopulationSerializer
    queryset = ReligiousPopulationModel.objects.all()