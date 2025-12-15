from django.db import models
from accounts.models import User as CustomUser # Assuming custom user model is correctly imported

class Post(models.Model):
    """
    Model for a social media post.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class Comment(models.Model):
    """
    Model for comments on a post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"

class Like(models.Model):
    """
    Model for a user liking a post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can only like a post once
        unique_together = ('user', 'post')
        ordering = ['-created_at']

    def __str__(self):
        return f"Like by {self.user.username} on Post {self.post.id}"
