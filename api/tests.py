from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import AppUser
from .serializers import AppUserSerializer
from django.core.files.uploadedfile import SimpleUploadedFile

class AppUsersGetTest(APITestCase):

    """
    Testing getting access to appUsers
    """

    def setUp(self):

        test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./api/test_data/profile_picture.jpg', 'rb').read(),
            content_type='image/jpeg'
            )

        self.sample_user = AppUser.objects.create(
            email='test@example.com',
            password='test123',
            name='Test User',
            bio='This is a test',
            gender='other',
            preferred_gender='other',
            localisation='test'
        )

    def test_list_appusers(self):
        """
        Ensures we can list all appUsers.
        """
        response = self.client.get(reverse('appuser-list'), format='json')
        appUsers = AppUser.objects.all()
        serializer = AppUserSerializer(appUsers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_specific_appuser_when_exists(self):
        """
        Ensures we can access an existing appUser
        """
        response = self.client.get(reverse('appuser-detail', kwargs={'pk': self.sample_user.pk}), format='json')
        appUsers = AppUser.objects.get(pk=self.sample_user.pk)
        serializer = AppUserSerializer(appUsers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_specific_appuser_when_doesnt_exists(self):
        """
        Expects a not found status when trying to access an appUser that doesn't exist
        """
        response = self.client.get(reverse('appuser-detail', kwargs={'pk': 10000}), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AppUsersCreateTest(APITestCase):

    """
    Testing getting access to appUsers
    """

    def setUp(self):

        self.url = reverse('appuser-list')

        test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./api/test_data/profile_picture.jpg', 'rb').read(),
            content_type='image/jpeg'
            )

        self.valid_sample_user = {
            'email': 'test@example.com',
            'password': 'test123',
            'name': 'Test User',
            'bio': 'This is a test',
            'picture': test_image,
            'gender': 'other',
            'preferred_gender':'other',
            'localisation': 'test'
            }

        self.invalid_sample_user1 = {
            'email': 'wrongemail',
            'password': 'test123',
            'name': 'Test User',
            'bio': 'This is a test',
            'picture': test_image,
            'gender': 'other',
            'preferred_gender':'other',
            'localisation': 'test'
            }

        self.invalid_sample_user2 = {
            'email': 'test@example.com',
            'password': 'test123',
            'bio': 'This is a test',
            'gender': 'other',
            'preferred_gender':'other',
            'localisation': 'test',
            'wrongField': 'test'
            }

        self.invalid_sample_user3 = {
            'email': 'test@example.com',
            'password': 'test123',
            'name': '',
            'bio': 'This is a test',
            'picture': test_image,
            'gender': 'other',
            'preferred_gender':'other',
            'localisation': 'test'
            }

    def test_create_appuser_when_valid(self):
        """
        Ensure we can create a new appUser when all fields are valid
        """
        response = self.client.post(self.url, self.valid_sample_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AppUser.objects.count(), 1)
        self.assertEqual(AppUser.objects.get().email, 'test@example.com')

    def test_create_appuser_when_email_invalid(self):
        """
        Ensure there is an error when creating a new appUser whith invalid email
        """
        response = self.client.post(self.url, self.invalid_sample_user1)
        self.assertEqual(response.status_code, 400)

    def test_create_appuser_when_field_missing(self):
        """
        Ensure there is an error when creating a new appUser whith missing fields
        """
        response = self.client.post(self.url, self.invalid_sample_user2)
        self.assertEqual(response.status_code, 400)

    def test_create_appuser_when_name_empty(self):
        """
        Ensure there is an error when creating a new appUser whith an empty name
        """
        response = self.client.post(self.url, self.invalid_sample_user3)
        self.assertEqual(response.status_code, 400)