from django.contrib import admin
from .models import Artist, Song, Album, Record_Company

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Record_Company)