from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm 


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

# GET, POST
def contact(request):

    # Check an incoming request 
    # and form sent by client should be "POST"
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Redirect to homepage
            return redirect('/')
    
    else:
        # If not POST, display blank form
        form = ContactForm()

    return render(request,
                  'blog/contact.html',
                  {'form': form})

  



