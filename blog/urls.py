from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.postdetail, name='postdetail'),
    path('post/delete/<int:pk>/', views.deletepost, name='deletepost'),
    path('post/new/', views.newpost, name='post_new'),
    path('accounts/', include('django.contrib.auth.urls')),
]