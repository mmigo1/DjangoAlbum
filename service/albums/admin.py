from django.contrib import admin

# Register your models here.
from .models import Performer, Album, Song


class PerformersAdmin(admin.ModelAdmin):
    model = Performer
    list_display_links = ('id', 'name')
    list_display = ['id', 'name']
    ordering = ('id',)

    # @admin.display(description='Альбомы исполнителя')
    # def get_albums(self, obj):
    #     return [album.name for album in obj.album_set.all()]


admin.site.register(Performer, PerformersAdmin)


class AlbumsAdmin(admin.ModelAdmin):
    model = Album
    list_display_links = ('id', 'name')
    list_display = ['id', 'name', 'released_date']
    ordering = ('id',)

    # @admin.display(description='Исполнитель')
    # def get_performer(self, obj):
    #     return [performer.name for performer in obj.performer.all()]


admin.site.register(Album, AlbumsAdmin)


class SongsAdmin(admin.ModelAdmin):
    model = Song
    list_display_links = ('id', 'name')
    list_display = ['id', 'name', 'number']
    ordering = ('id',)

    # @admin.display(description='Альбом')
    # def get_albums(self, obj):
    #     return [album.name for album in obj.album.all()]


admin.site.register(Song, SongsAdmin)
