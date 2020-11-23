from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

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


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PotentialMatchesViewSet(viewsets.ModelViewSet):

    queryset = AppUser.objects.all().order_by('email')
    serializer_class = AppUserSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):

        queryset = None

        try:
            gender = self.request.query_params.get('gender')
            preferred_gender = self.request.query_params.get('preferredGender')
            location = self.request.query_params.get('location')
            email = self.request.query_params.get('email')

            queryset = AppUser.objects.filter(
                gender=preferred_gender,
                preferred_gender=gender,
                localisation=location
               ).exclude(email=email).order_by('email')

        except Exception as e:
            print(f"Error - could not filter results due to missing request parameters: {e}")

        return queryset

