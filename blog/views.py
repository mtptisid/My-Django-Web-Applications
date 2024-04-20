from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm


posts =[
    {
        'author':'Siddharth M',
        'title': 'What is Django',
        'content':"Django is a powerful web framework for building web applications quickly and efficiently. It follows the Don't Repeat Yourself (DRY) principle and is designed to make common tasks simple and robust.",
        'date_posted':'05 April 2024 '

    },
    {
        'author':'Siddhart M',
        'title': 'Set Up Django',
        'content':"Setting up Django is a breeze! With just a few simple steps, you can have a new Django project up and running in no time. Let's walk through the installation and project setup",
        'date_posted':'05 April 2024 '
    },

 
]

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/Home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():  
            user = form.get_user()
            login(request, user)
            return redirect('/Home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


@login_required
def Home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# Create your views here.

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})