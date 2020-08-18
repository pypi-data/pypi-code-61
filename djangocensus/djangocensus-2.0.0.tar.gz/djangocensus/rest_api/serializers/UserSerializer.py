from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


# Your serializers goes here.
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
