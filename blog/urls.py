from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.postdetail, name='postdetail'),
    path('post/delete/<int:pk>/', views.deletepost, name='deletepost'),
    path('post/new/', views.newpost, name='post_new'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)