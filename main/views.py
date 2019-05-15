from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
import omdb
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .serializers import UserSerializer, MovieSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



API_KEY='e15e114e'
omdb.set_default('apikey',API_KEY)
def land(request):

    return render(request,'landing.html')
@login_required
def list_films(request):

    films_list=Movie.objects.all()
    paginator = Paginator(films_list, 15)
    page = request.GET.get('page', 1)

    films_list=paginator.get_page(page)



    return render(request,'film_list.html',{'films':films_list})
@login_required
def new_film(request):
    form=MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(list_films)
    return render(request, 'new_movie.html', {'form':form})
@login_required
def edit_movie(request,id):
    film=get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None,instance=film)
    if form.is_valid():
        form.save()
        return redirect(list_films)
    return render(request, 'new_movie.html', {'form': form})
@login_required
def delete_movie(request, id):
    film= get_object_or_404(Movie,pk=id)
    if request.method =="POST" or request.method=="GET":
        film.delete()
        return redirect(list_films)
    return render(request,'accept.html',{'film':film})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(list_films)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def features(request):
    return render(request, 'features.html')