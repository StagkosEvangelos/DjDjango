from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import Album,Song,Artist,EmailForm


def Album_List(request):

    q = request.GET.get('q','')

    if (q==''):
        albums = Album.objects.order_by('date_of_release')

    else:
        albums = Album.objects.filter(album_title__contains=q).order_by('date_of_release')

    return render(request,'djdjango/album_list.html', {'albums': albums})


def AlbumDetail(request,pk):
    album_detail=get_object_or_404(Album,pk=pk)
    return  render(request,'djdjango/detail.html',{'album_detail':album_detail})

def Contact(request):
    return render(request,'djdjango/contact.html')

class DetailView(generic.DeleteView):
    model=Album
    template_name = 'djdjango/detail.html'

def Home(request):
    home = Album.objects.order_by('-created')
    return render(request,'djdjango/homepage.html', {'home': home})

def Artist_List(request):
    artist_list=Artist.objects.order_by('artist_name')
    return render(request, 'djdjango/artist_list.html', {'artist_list':artist_list})

def ArtistAlbum(request,pk):
    artist_get=get_object_or_404(Artist,pk=pk)
    artist_album=Album.objects.filter(artist=artist_get)
    return  render(request,'djdjango/artist_album.html',{'artist_album':artist_album})

def punkView(request):
    punk=Album.objects.filter(genre='punk')
    return  render(request,'djdjango/punk.html',{'punk':punk})

def rockView(request):
    rock=Album.objects.filter(genre='rock')
    return  render(request,'djdjango/rock.html',{'rock':rock})

def metalView(request):
    metal=Album.objects.filter(genre='metal')
    return  render(request,'djdjango/metal.html',{'metal':metal})

def swingView(request):
    swing=Album.objects.filter(genre='swing')
    return  render(request,'djdjango/swing.html',{'swing':swing})

def electroView(request):
    electro=Album.objects.filter(genre='electro')
    return  render(request,'djdjango/electro.html',{'electro':electro})

def popView(request):
    pop=Album.objects.filter(genre='pop')
    return  render(request,'djdjango/pop.html',{'pop':pop})


def sendmail(request):
      if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
          firstname = form.cleaned_data['firstname']
          lastname = form.cleaned_data['lastname']
          email = form.cleaned_data['email']
          subject = form.cleaned_data['subject']
          botcheck = form.cleaned_data['botcheck'].lower()
          message = form.cleaned_data['message']
          if botcheck == 'yes':
            try:
              fullemail = firstname + " " + lastname + " " + "<" + email + ">"
              send_mail(subject, message, fullemail, ['eyagstag@gmail.com'])
              return HttpResponseRedirect('/email/thankyou/')
            except:
              return HttpResponseRedirect('/email/')
        else:
          return HttpResponseRedirect('/email/')
      else:
        return HttpResponseRedirect('/email/')

#SEARCH ALBUMS ALPHABETICAL
def ASearch(request):
    A_search=Album.objects.filter(album_title__istartswith='a')
    return render(request,'djdjango/search_album/A.html',{'A_search':A_search})

def BSearch(request):
    B_search=Album.objects.filter(album_title__istartswith='b')
    return render(request,'djdjango/search_album/B.html',{'B_search':B_search})

def CSearch(request):
    C_search=Album.objects.filter(album_title__istartswith='c')
    return render(request,'djdjango/search_album/C.html',{'C_search':C_search})

def DSearch(request):
    D_search=Album.objects.filter(album_title__istartswith='d')
    return render(request,'djdjango/search_album/D.html',{'D_search':D_search})

def ESearch(request):
    E_search=Album.objects.filter(album_title__istartswith='e')
    return render(request,'djdjango/search_album/E.html',{'E_search':E_search})

def FSearch(request):
    F_search=Album.objects.filter(album_title__istartswith='f')
    return render(request,'djdjango/search_album/F.html',{'F_search':F_search})

def GSearch(request):
    G_search=Album.objects.filter(album_title__istartswith='g')
    return render(request,'djdjango/search_album/G.html',{'G_search':G_search})

def HSearch(request):
    H_search=Album.objects.filter(album_title__istartswith='h')
    return render(request,'djdjango/search_album/H.html',{'H_search':H_search})

def ISearch(request):
    I_search=Album.objects.filter(album_title__istartswith='i')
    return render(request, 'djdjango/search_album/I.html', {'I_search':I_search})

def JSearch(request):
    J_search=Album.objects.filter(album_title__istartswith='j')
    return render(request,'djdjango/search_album/J.html',{'J_search':J_search})

def KSearch(request):
    K_search=Album.objects.filter(album_title__istartswith='k')
    return render(request,'djdjango/search_album/K.html',{'K_search':K_search})

def LSearch(request):
    L_search=Album.objects.filter(album_title__istartswith='l')
    return render(request,'djdjango/search_album/L.html',{'L_search':L_search})

def MSearch(request):
    M_search=Album.objects.filter(album_title__istartswith='m')
    return render(request,'djdjango/search_album/M.html',{'M_search':M_search})

def NSearch(request):
    N_search=Album.objects.filter(album_title__istartswith='n')
    return render(request,'djdjango/search_album/N.html',{'N_search':N_search})

def OSearch(request):
    O_search=Album.objects.filter(album_title__istartswith='o')
    return render(request,'djdjango/search_album/O.html',{'O_search':O_search})

def PSearch(request):
    P_search=Album.objects.filter(album_title__istartswith='p')
    return render(request,'djdjango/search_album/P.html',{'P_search':P_search})

def QSearch(request):
    Q_search=Album.objects.filter(album_title__istartswith='q')
    return render(request,'djdjango/search_album/Q.html',{'Q_search':Q_search})

def RSearch(request):
    R_search=Album.objects.filter(album_title__istartswith='r')
    return render(request,'djdjango/search_album/R.html',{'R_search':R_search})

def SSearch(request):
    S_search=Album.objects.filter(album_title__istartswith='s')
    return render(request,'djdjango/search_album/S.html',{'S_search':S_search})

def TSearch(request):
    T_search=Album.objects.filter(album_title__istartswith='t')
    return render(request,'djdjango/search_album/T.html',{'T_search':T_search})

def USearch(request):
    U_search=Album.objects.filter(album_title__istartswith='u')
    return render(request,'djdjango/search_album/U.html',{'U_search':U_search})

def VSearch(request):
    V_search=Album.objects.filter(album_title__istartswith='v')
    return render(request,'djdjango/search_album/V.html',{'V_search':V_search})

def WSearch(request):
    W_search=Album.objects.filter(album_title__istartswith='w')
    return render(request,'djdjango/search_album/W.html',{'W_search':W_search})

def XSearch(request):
    X_search=Album.objects.filter(album_title__istartswith='x')
    return render(request,'djdjango/search_album/X.html',{'X_search':X_search})

def YSearch(request):
    Y_search=Album.objects.filter(album_title__istartswith='y')
    return render(request,'djdjango/search_album/Y.html',{'Y_search':Y_search})

def ZSearch(request):
    Z_search=Album.objects.filter(album_title__istartswith='z')
    return render(request,'djdjango/search_album/Z.html',{'Z_search':Z_search})




