from django.shortcuts import render
from rest_framework import viewsets
from .models import Album, Performer, Song
from .serializers import PerformerSerializer, SongSerializer, AlbumSerializer



# Create your views here.

# ------------ API -----------------


class PerformerApiView(viewsets.ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer


class AlbumApiView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongApiView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
