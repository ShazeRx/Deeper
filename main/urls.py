
from django.urls import path
from .views import list_films, new_film, edit_movie, delete_movie, signup, features
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'top', views.TopViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('filmy/', list_films, name='list_films' ),
    path('signup/', signup, name='signup'),
    path('new_movie/', new_film, name='new_film' ),
    path('edit_movie/<int:id>/', edit_movie,name='edit_movie' ),
    path('delete_movie/<int:id>/', delete_movie, name='delete_movie' ),
    path('features/', features, name='features' ),




]
