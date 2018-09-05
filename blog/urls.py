from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.postdetail, name='postdetail'),
    path('post/new/', views.newpost, name='post_new'),
]