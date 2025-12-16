from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Connection(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('blocked', 'Blocked'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='connections_initiated',
        on_delete=models.CASCADE
    )
    connection = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='connections_received',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'connection')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} -> {self.connection} ({self.status})"


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        on_delete=models.CASCADE
    )
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_company_post = models.BooleanField(default=False)
    
    # Simple likes count or M2M can be added
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.user} at {self.created_at}"

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='post_comments',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
