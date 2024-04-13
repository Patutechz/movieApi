from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    about = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title