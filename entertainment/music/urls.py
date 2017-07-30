from django.conf.urls import url

from . import views

app_name = 'music'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<artist_name_slug>[\w\-]+)$', views.show_albums, name='detail'),
    url(r'^album/(?P<album_name_slug>[\w\-]+)$', views.show_songs, name='songs'),
]