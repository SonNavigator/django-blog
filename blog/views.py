from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    # Get all posts
    posts = Post.objects.all()
    return render(request, 
                  'blog/index.html',
                  {'posts': posts})


def blog_detail(request, id):
    # Get one post
    post = Post.objects.get(id=id)
    return render(request, 
                  'blog/blog-details.html',
                  {'post': post})

  



