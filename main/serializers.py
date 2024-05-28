from rest_framework import serializers
from .models import (Biz_haqimizda,
                     Comment,
                     User,
                     Profile,
                     Team,
                     Social_media,
                     Book,
                     Category)

class Biz_haqimizdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biz_haqimizda
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class Social_mediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')



