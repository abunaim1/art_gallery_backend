from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

class ArtistViewset(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
