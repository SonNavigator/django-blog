from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm, RegisterForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm


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
@login_required(login_url='/sign-in')
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
            return HttpResponse("Please correct you form")
    
    else:
        # If not POST, display blank form
        form = ContactForm()

    return render(request,
                  'blog/contact.html',
                  {'form': form})


# Week 4 Search
def search(request):
    # Get an incoming query string sent by client
    search_post = request.GET.get('q')
    if search_post:
        # Query data from the database if matched
        post = Post.objects.filter(Q(title__contains=search_post))
    else:
        # Redirect to homepage
        return redirect('/')

    return render(request, 'blog/search.html', {'post': post})


def sign_in(request):
    if request.method == "POST":
        # print("I am signing in")
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Incorrect username or password')
            return redirect('/sign-in')

    else:
        form = AuthenticationForm()
        return render(request, 'blog/login.html',
                               {'form': form})


def sign_out(request):
    logout(request)
    return redirect('/')


# Create your views here.
def sign_up(request):
    if request.method == "POST":
	    form = RegisterForm(request.POST)
	    if form.is_valid():
	        form.save()
	        return redirect("/sign-in")
    else:
	    form = RegisterForm()
    return render(request, "blog/register.html", {"form":form})



    

  



