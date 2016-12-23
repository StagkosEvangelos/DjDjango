from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from .models import Album,Song


def Album_List(request):
    albums=Album.objects.order_by('album_title')
    return render(request, 'djdjango/album_list.html', {'albums':albums})

def AlbumDetail(request,pk):
    album_detail=get_object_or_404(Album,pk=pk)
    return  render(request,'djdjango/detail.html',{'album_detail':album_detail})