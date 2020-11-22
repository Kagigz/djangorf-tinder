from rest_framework import serializers
from .models import AppUser, GENDERS


class AppUserSerializer(serializers.ModelSerializer):
    preferred_gender = serializers.ChoiceField(choices=GENDERS, default='male')
    gender = serializers.ChoiceField(choices=GENDERS, default='male')
    picture = serializers.ImageField(allow_null=True)

    class Meta:
        model = AppUser
        fields = "__all__"