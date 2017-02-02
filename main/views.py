from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Album,Song


def Album_List(request):
    albums=Album.objects.order_by('album_title')
    return render(request, 'djdjango/album_list.html', {'albums':albums})

def AlbumDetail(request,pk):
    album_detail=get_object_or_404(Album,pk=pk)
    return  render(request,'djdjango/detail.html',{'album_detail':album_detail})

def Contact(request):
    return render(request,'djdjango/contact.html')

class DetailView(generic.DeleteView):
    model=Album
    template_name = 'djdjango/detail.html'

def Home(request):
    return render(request,'djdjango/homepage.html')
