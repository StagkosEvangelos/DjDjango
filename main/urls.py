from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.Album_List, name='album_list'),
    #url(r'album/$', views.IndexView.as_view(), name='album'),
    #url(r'^(?P<pk>[0-9]+)/$', views.AlbumDetail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^contact/$',views.Contact,name='contact'),
    url(r'^home/$',views.Home,name='home'),
]
