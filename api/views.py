from rest_framework import viewsets

from .serializers import AppUserSerializer
from .models import AppUser


class AppUserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.

    delete:
    Remove an existing user.

    partial_update:
    Update one or more fields on an existing user.

    update:
    Update a user.
    """
    queryset = AppUser.objects.all().order_by('email')
    serializer_class = AppUserSerializer
