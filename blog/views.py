from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    data = {'posts': posts}
    return render(request, 'blog/post_list.html', data)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {'post': post}
    return render(request, 'blog/post_detail.html', data)

def post_new(request):
    form = PostForm()
    data = {'form': form}
    return render(request, 'blog/post_edit.html', data)

def page_not_found(request, exception):
    return render(request, 'blog/page_not_found.html', status=404)

def page_server_error(request):
    return render(request, 'blog/page_server_error.html', status=500)
