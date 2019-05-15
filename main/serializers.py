from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email','password')
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','name','description','year','released')


