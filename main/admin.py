from django.contrib import admin
from .models import Movie
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('name','description','year','released','rating','photo')
    list_display = ('name','description','year','released')
    list_filter = ('year','released','rating')
    search_fields = ('name','description')
