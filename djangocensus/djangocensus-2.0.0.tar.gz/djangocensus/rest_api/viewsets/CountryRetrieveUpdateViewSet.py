from rest_framework.generics import RetrieveUpdateAPIView
from djangocensus.models.CountryModel import CountryModel
from djangocensus.rest_api.serializers import CountrySerializer


# Create viewset goes here.
class CountryRetrieveUpdateViewSet(RetrieveUpdateAPIView):
    serializer_class = CountrySerializer
    queryset = CountryModel.objects.all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"