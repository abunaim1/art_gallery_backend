from rest_framework import serializers
from . import models
from artist.serializers import ArtistSerializer

class ArtWorkSerializers(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = models.Artwork
        fields = '__all__'