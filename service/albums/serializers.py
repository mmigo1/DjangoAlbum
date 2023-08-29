from rest_framework import serializers

from .models import Performer, Song, Album


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'
        depth = 1


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        depth = 1


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        depth = 1
