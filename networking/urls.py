from django.urls import path
from . import views

app_name = 'networking'

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('network/', views.network, name='network'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
]
