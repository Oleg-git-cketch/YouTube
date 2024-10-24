from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.category_name)


class Video(models.Model):
    video_title = models.CharField(max_length=128)
    video_content = models.ImageField(upload_to='media')
    user = models.IntegerField()
    like = models.TextField()
    dislike = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.video_title)