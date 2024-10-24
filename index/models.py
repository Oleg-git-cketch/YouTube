from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Video(models.Model):
    video_title = models.CharField(max_length=128)
    video_content = models.ImageField(upload_to='media')
    video_video = models.FileField(upload_to='videos')
    user = models.TextField()
    like = models.TextField()
    dislike = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.video_title)

class User(models.Model):
    user_name = models.CharField(max_length=32)
    phone_number = models.IntegerField()
    email = models.EmailField()
    password = models.TextField()
    password2 = models.TextField()

    def __str__(self):
        return str(self.user_name)
