from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields for the custom user model
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.URLField(max_length=200, blank=True, null=True)
    
    # ManyToMany field for followers (a user follows another user)
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following', 
        blank=True
    )

    def __str__(self):
        return self.username
