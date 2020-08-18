from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from djangocensus.rest_api.serializers import UserSerializer


# Detail viewset goes here.
class UserDetailViewSet(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()