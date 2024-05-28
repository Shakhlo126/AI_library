from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('biz_haqimizda/', Biz_haqimizdaAPIView.as_view(), name='biz_haqimizda'),
    path('comment/', CommentAPIView.as_view(), name='comment'),
    path('user/', UserAPIView.as_view(), name='user'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('team/', TeamAPIView.as_view(), name='team'),
    path('social_media/', Social_mediaAPIView.as_view(), name='social_media'),
    path('books/', BookAPIView.as_view(), name='books'),
    path('category/', CategoryAPIView.as_view(), name='category'),
]
