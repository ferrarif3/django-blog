from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'postlist.html', {'posts': posts})
