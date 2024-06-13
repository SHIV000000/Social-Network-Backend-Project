from django.db import models
from users.models import CustomUser

class Hashtag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Discussion(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='discussions')
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='discussions')
    created_on = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_comments')

    def __str__(self):
        return self.text
