from rest_framework.generics import RetrieveUpdateAPIView
from djangocensus.models.StateModel import StateModel
from djangocensus.rest_api.serializers import StateSerializer


# Create viewset goes here.
class StateRetrieveUpdateViewSet(RetrieveUpdateAPIView):
    serializer_class = StateSerializer
    queryset = StateModel.objects.all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"