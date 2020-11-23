from django.db import models

from PIL import Image, ImageFilter
from uuid import uuid4
from background_task import background
from datetime import datetime, timedelta

GENDERS = (
    ('female', 'Female'),
    ('male', 'Male'),
    ('nonbinary', 'Non-binary'),
    ('other', 'Other')
)

class AppUser(models.Model):
    """
    User profiles
    """

    email = models.EmailField()
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    picture = models.ImageField(upload_to="userpictures/")
    gender = models.CharField(max_length=30, choices=GENDERS)
    preferred_gender = models.CharField(max_length=30, choices=GENDERS)
    localisation = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)


    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(AppUser, self).save(*args, **kwargs)
        try:
            picture_path = self.picture.path
            self.modify_picture(picture_path)
        except Exception as e:
            print(f"Error modifying profile picture: {e}")

    def modify_picture(self, path, thumbnail_size=(600, 600), blur_radius=5):
        """
        Resizes profile picture to thumbnail_size, blurs it and saves it to a new location

        Parameters:
        path (string): picture path
        thumbnail_size (int, int): size of the new picture (600x600 by default)
        blur_radius (int): blur radius for the gaussian blur filter (5 by default)

        """
        img = Image.open(path)
        img.thumbnail(thumbnail_size)
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
        blurred_img.save(path)


class Match(models.Model):
    """
    Matches between users
    """

    user1 = models.ForeignKey(AppUser, related_name='user1_set', on_delete=models.CASCADE)
    user2 = models.ForeignKey(AppUser, related_name='user2_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    match_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    
    def __str__(self):
        return f"{self.user1.__str__()} x {self.user2.__str__()}"

    @background(schedule=60*60-24)
    def delete_old_matches(self):
        """
        Delete matches older than 14 days
        """
        NUMBER_OF_DAYS = 14

        try:
            old_matches = Match.object.all().filter(
                created__gte=datetime.now()-60*60*24*NUMBER_OF_DAYS
            )
            old_matches.delete()
            print(f"Deleted {len(old_matches)} old matches")
        except Exception as e:
            print(f"Error deleting old matches: {e}")

