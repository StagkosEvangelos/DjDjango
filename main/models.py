from django.db import models
from django.core.urlresolvers import reverse
from django import forms


class Artist(models.Model):
    artist_name = models.CharField(max_length=4000)
    is_band = models.BooleanField()
    artist_photo = models.CharField(max_length=1000)
    profile = models.CharField(max_length=4000)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.artist_name


class Record_Company(models.Model):
    company_name = models.CharField(max_length=250)
    location = models.CharField(max_length=1000)
    contact = models.CharField(max_length=250)
    founding = models.DateField()
    profile = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.company_name


class Album(models.Model):
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=500)
    style = models.CharField(max_length=100)
    date_of_release = models.DateField()
    total_duration = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    profile = models.CharField(max_length=4000)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True)
    record_company = models.ForeignKey(Record_Company, on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)


    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title


class Song(models.Model):
    song_title = models.CharField(max_length=250)
    date_of_release = models.DateField()
    total_duration = models.CharField(max_length=100)
    song_link = models.CharField(max_length=1000)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.song_title

class EmailForm(forms.Form):
  firstname = forms.CharField(max_length=255)
  lastname = forms.CharField(max_length=255)
  email = forms.EmailField()
  subject = forms.CharField(max_length=255)
  botcheck = forms.CharField(max_length=5)
  message = forms.CharField()