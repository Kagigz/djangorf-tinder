from django.db import models
from django.conf import settings

class AppUser(models.Model):
    """
    User profiles
    """
    email = models.EmailField()
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    picture = models.ImageField(upload_to="userpictures/")
    gender = models.CharField(max_length=30,
                choices=[
                    ('female','Female'),
                    ('male','Male'),
                    ('nonbinary','Non-binary'),
                    ('other','Other')
                    ])
    localisation = models.CharField(max_length=200)

    def __str__(self):
        return self.email