from django.shortcuts import render
from rest_framework import generics , viewsets
from .models import (Biz_haqimizda,
                     Comment,
                     User,
                     Profile,
                     Team,
                     Social_media,
                     Book,
                     Category)
from .serializers import (Biz_haqimizdaSerializer,
                          CommentSerializer,
                          UserSerializer,
                          ProfileSerializer,
                          TeamSerializer,
                          Social_mediaSerializer,
                          BookSerializer,
                          CategorySerializer)
# Create your views here.
class Biz_haqimizdaAPIView(generics.ListAPIView):
    queryset = Biz_haqimizda.objects.all()
    serializer_class = Biz_haqimizdaSerializer

class CommentAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class Social_mediaAPIView(generics.ListAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaSerializer

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class HomeAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer