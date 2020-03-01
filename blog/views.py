from django.shortcuts import render, redirect, get_object_or_404
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

def save_post(request_post_new, instance_post=None):
    form = PostForm(request_post_new.POST, instance=instance_post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request_post_new.user
        post.save()
        return redirect('post_detail', pk=post.pk)

def post_new(request):
    if request.method == 'POST':
        return save_post(request)
    else:
        form = PostForm()
        data = {'form': form}
        return render(request, 'blog/post_edit.html', data)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        return save_post(request, post)
    else:
        form = PostForm(instance=post)
        data = {'form': form}
        return render(request, 'blog/post_edit.html', data)

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('create_date')
    data = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', data)

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def page_not_found(request, exception):
    return render(request, 'blog/page_not_found.html', status=404)

def page_server_error(request):
    return render(request, 'blog/page_server_error.html', status=500)
