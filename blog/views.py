from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'postlist.html', {'posts': posts})


def postdetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'postdetail.html', {'post': post})