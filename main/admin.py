from django.contrib import admin
from .models import Artist, Song, Album, Record_Company

class Search_Album(admin.ModelAdmin):
    list_display = ["album_title", "created", "updated"]
    list_filter = ["genre"]
    search_fields = ["album_title"]
    class Meta:
        model = Album

class Search_Artist(admin.ModelAdmin):
    list_display = ["artist_name", "created", "updated"]
    search_fields = ["artist_name"]
    class Meta:
        model = Artist

class Search_Song(admin.ModelAdmin):
    list_display = ["song_title", "created", "updated"]
    search_fields = ["song_title"]
    class Meta:
        model = Song

class Search_Record_Company(admin.ModelAdmin):
    list_display = ["company_name", "created", "updated"]
    search_fields = ["company_name"]
    class Meta:
        model = Record_Company


admin.site.register(Artist, Search_Artist)
admin.site.register(Song, Search_Song)
admin.site.register(Album, Search_Album)
admin.site.register(Record_Company, Search_Record_Company)




