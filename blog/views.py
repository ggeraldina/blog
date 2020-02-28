from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    date = { 'posts': posts }
    return render(request, 'blog/post_list.html', date)

def page_not_found(request, exception):
    return render(request, 'blog/page_not_found.html', status=404)
