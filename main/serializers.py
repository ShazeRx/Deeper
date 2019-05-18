from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Comment
from drf_dynamic_fields import DynamicFieldsMixin

import omdb
API_KEY='e15e114e'
omdb.set_default('apikey',API_KEY)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email','password')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields=('movie','user','timestamp','content','approved')
        read_only_fields = ('approved',)
class MovieSerializer(DynamicFieldsMixin,serializers.HyperlinkedModelSerializer):
    comments=CommentSerializer(many=True,default=0,read_only=True)
    comments_count=serializers.IntegerField(read_only=True)
    rank=serializers.IntegerField(read_only=True)


    class Meta:
        model = Movie

        fields = ('id','name','description','year','released','comments','rating','rank','comments_count')
        read_only_fields = ('id','description','year','rating','released')

    def validate_name(self, value):
        data=omdb.get(title=value)
        if data:
            print(data['title'])



            return value
        else:
            raise serializers.ValidationError("Film not Found")
    def create(self, validated_data):
        movie=Movie.objects.create(name=validated_data['name'],
                                  description=omdb.get(title=validated_data['name'])['type'],
                                  year=omdb.get(title=validated_data['name'])['year'],
                                    released=omdb.get(title=validated_data['name'])['year'],

                                  rating=omdb.get(title=validated_data['name'])['imdb_rating'])
        movie.save()
        return movie










