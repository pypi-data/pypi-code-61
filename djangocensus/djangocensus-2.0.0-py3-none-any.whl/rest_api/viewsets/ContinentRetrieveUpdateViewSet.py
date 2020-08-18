from rest_framework.generics import RetrieveUpdateAPIView
from djangocensus.models.ContinentModel import ContinentModel
from djangocensus.rest_api.serializers import ContinentSerializer


# Create viewset goes here.
class ContinentRetrieveUpdateViewSet(RetrieveUpdateAPIView):
    serializer_class = ContinentSerializer
    queryset = ContinentModel.objects.all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"