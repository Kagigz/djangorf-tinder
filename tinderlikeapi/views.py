from rest_framework import viewsets

from .serializers import AppUserSerializer
from .models import AppUser


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all().order_by('email')
    serializer_class = AppUserSerializer