from django.contrib import admin
from .models import Movie, Comment
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('name','description','year','released','rating','photo')
    list_display = ('name','description','year','released')
    list_filter = ('year','released','rating')
    search_fields = ('name','description')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('movie', 'content', 'timestamp','user')
    list_display = ('movie', 'timestamp', 'user','approved')
    list_filter = ('movie', 'timestamp')
    search_fields = ('movie',)

