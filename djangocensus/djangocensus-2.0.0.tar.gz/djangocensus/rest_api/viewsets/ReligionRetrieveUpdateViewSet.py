from rest_framework.generics import RetrieveUpdateAPIView
from djangocensus.models.ReligionModel import ReligionModel
from djangocensus.rest_api.serializers import ReligionSerializer


# Create viewset goes here.
class ReligionRetrieveUpdateViewSet(RetrieveUpdateAPIView):
    serializer_class = ReligionSerializer
    queryset = ReligionModel.objects.all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"