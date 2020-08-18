from rest_framework.generics import CreateAPIView
from djangocensus.models.PopulationModel import PopulationModel
from djangocensus.rest_api.serializers import PopulationSerializer


# Create viewset goes here.
class PopulationCreateViewSet(CreateAPIView):
    serializer_class = PopulationSerializer
    queryset = PopulationModel.objects.all()