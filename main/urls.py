from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^artist/$',views.Artist_List,name='artist_list'),
    #url(r'album/$', views.IndexView.as_view(), name='album'),
    #url(r'^(?P<pk>[0-9]+)/$', views.AlbumDetail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^artist/(?P<pk>[0-9]+)/$',views.ArtistAlbum,name='artist_album'),
    url(r'^contact/$',views.Contact,name='contact'),
    url(r'^albums/$',views.Album_List,name='album_list'),
    url(r'^punk/$',views.punkView,name='punk'),
    url(r'^rock/$',views.rockView,name='rock'),
    url(r'^metal/$',views.metalView,name='metal'),
    url(r'^swing/$',views.swingView,name='swing'),
    url(r'^electro/$',views.electroView,name='electro'),
    url(r'^pop/$',views.popView,name='pop'),

    #SEARCH ALBUMS ALPHABETICAL
    url(r'^albums/A/$',views.ASearch,name='A_search'),
    url(r'^albums/B/$',views.BSearch,name='B_search'),
    url(r'^albums/C/$',views.CSearch,name='C_search'),
    url(r'^albums/D/$', views.DSearch, name='D_search'),
    url(r'^albums/E/$', views.ESearch, name='E_search'),
    url(r'^albums/F/$', views.FSearch, name='F_search'),
    url(r'^albums/G/$', views.GSearch, name='G_search'),
    url(r'^albums/H/$', views.HSearch, name='H_search'),
    url(r'^albums/I/$', views.ISearch, name='I_search'),
    url(r'^albums/K/$', views.JSearch, name='J_search'),
    url(r'^albums/K/$', views.KSearch, name='K_search'),
    url(r'^albums/L/$', views.LSearch, name='L_search'),
    url(r'^albums/M/$', views.MSearch, name='M_search'),
    url(r'^albums/N/$', views.NSearch, name='N_search'),
    url(r'^albums/O/$', views.OSearch, name='O_search'),
    url(r'^albums/P/$', views.PSearch, name='P_search'),
    url(r'^albums/Q/$', views.QSearch, name='Q_search'),
    url(r'^albums/R/$', views.RSearch, name='R_search'),
    url(r'^albums/S/$', views.SSearch, name='S_search'),
    url(r'^albums/T/$', views.TSearch, name='T_search'),
    url(r'^albums/U/$', views.USearch, name='U_search'),
    url(r'^albums/V/$', views.VSearch, name='V_search'),
    url(r'^albums/W/$', views.WSearch, name='W_search'),
    url(r'^albums/X/$', views.XSearch, name='X_search'),
    url(r'^albums/Y/$', views.YSearch, name='Y_search'),
    url(r'^albums/Z/$', views.ZSearch, name='Z_search'),

]

