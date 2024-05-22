from django.db import models
from artist.models import Artist

class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    art_image = models.ImageField(upload_to='uploads/artGallery/', blank=True, null=True)