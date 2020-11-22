from rest_framework import serializers
from .models import AppUser


class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'email', 'password', 'name', 'bio', 'picture', 'gender', 'localisation')