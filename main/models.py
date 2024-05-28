from django.db import models

# Create your models here.
class Social_media(models.Model):
    tg_link = models.URLField()
    insta_link = models.URLField()
    youtube_link = models.URLField()
    linkedin_link = models.URLField()
    facebook_link = models.URLField()
    tiktok_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tg_link


class Biz_haqimizda(models.Model):
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    video = models.FileField(upload_to="videos/")
    social_media = models.ForeignKey(Social_media, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    mini_description = models.TextField()
    book_link = models.URLField()
    catgory = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    birthday = models.DateField()
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    image = models.ImageField(upload_to="images/")
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    portfolio_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
