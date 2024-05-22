from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ArtworkViewset(viewsets.ModelViewSet):
    queryset = models.Artwork.objects.all()
    serializer_class = serializers.ArtWorkSerializers