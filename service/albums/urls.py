from django.urls import path, include
from rest_framework import routers
from .views import PerformerApiView, AlbumApiView, SongApiView

router = routers.DefaultRouter()
router.register(r'api/album', AlbumApiView)
router.register(r'api/song', SongApiView)
router.register(r'api/performer', PerformerApiView)

urlpatterns = [
    path('', include(router.urls)),
]
