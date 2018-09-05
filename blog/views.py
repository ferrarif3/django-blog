from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'postlist.html', {'posts': posts})


def postdetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'postdetail.html', {'post': post})


def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('postdetail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'newpost.html', {'form': form})