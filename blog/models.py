from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # This must exist for PostForm to work with tags
    tags = TaggableManager()

    def __str__(self):
        return self.title
