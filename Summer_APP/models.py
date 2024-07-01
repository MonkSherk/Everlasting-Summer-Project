from django.db import models

# Create your models here.
from django.db import models

class BackgroundImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.name

class Live_Wallpaper(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='video_wallpaper/')

    def __str__(self):
        return self.name
class MusicTrack(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/tracks/')

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='characters/')

    def __str__(self):
        return self.name
