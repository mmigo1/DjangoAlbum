from django.db import models


class Performer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Исполнитель')

    albums = models.ManyToManyField('Album', related_name='Альбомы')

    def __str__(self):
        return f'{self.name}'


class Album(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название альбома')
    released_date = models.DateField(verbose_name='Дата релиза', blank=True)

    songs = models.ManyToManyField('Song')

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название песни')
    number = models.IntegerField(verbose_name='Номер в альбоме')

    def __str__(self):
        return f'{self.name}'
