from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'postlist.html', {'posts': posts})


def postdetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'postdetail.html', {'post': post})


def deletepost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')


def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.image = request.FILES['image']
            post.save()
            return redirect('postdetail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'newpost.html', {'form': form})
