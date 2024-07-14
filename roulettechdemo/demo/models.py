from django.db import models

# Create your models here.

class Articles(models.Model):
    username = models.CharField(max_length=20)
    album_name = models.CharField(max_length=150)
    album_artist = models.CharField(max_length=150)
    article_text = models.CharField(max_length=1000)
    imageUrl = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.album_name

class Comments(models.Model):
    username = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete = models.CASCADE)
    def __str__(self):
        return self.comment