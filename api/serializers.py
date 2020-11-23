from rest_framework import serializers
from .models import AppUser, Match, GENDERS


class AppUserSerializer(serializers.ModelSerializer):
    preferred_gender = serializers.ChoiceField(choices=GENDERS, default='male')
    gender = serializers.ChoiceField(choices=GENDERS, default='male')
    picture = serializers.ImageField(allow_null=True)

    class Meta:
        model = AppUser
        fields = "__all__"

class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = "__all__"

