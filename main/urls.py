from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.Album_List, name='album_list'),
    #url(r'album/$', views.IndexView.as_view(), name='album'),
    url(r'^(?P<pk>[0-9]+)/$', views.AlbumDetail, name='detail'),
]
