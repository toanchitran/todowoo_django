from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.forms import *
from .models import Todos
from .form import TodoForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'error': 'That username is already taken. Please choose another username to signup. Thank you.'
                }
                return render(request, 'todo/signupuser.html', context)
        else:
            context = {
                'form': UserCreationForm(),
                'error': 'Your password and your confirmed password did not match. Please type again. Thank you'
            }
            return render(request, 'todo/signupuser.html', context)

def signInUser(request):
    if request.method == 'GET':
        return render(request, 'todo/signinuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username= request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {
                'form': UserCreationForm(),
                'error': 'The username and password did not match. Please login in again. Thank you'
            }
            return render(request, 'todo/signinuser.html', context)
        else:
            login(request, user)
            return redirect('home')

@login_required
def signOutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createTask(request):
    if request.method == 'GET':
        return render(request, 'todo/createnewtask.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=True)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            context = {
                'form': TodoForm(),
                'error': 'Bad value input. Please try again'
            }
            return render(request, 'todo/createnewtask.html', context)

@login_required
def currentTask(request):
    todos =  Todos.objects.filter(user = request.user, date_completed__isnull=True)
    return render(request, 'todo/currenttask.html', {'todos': todos})

@login_required
def completedTasks(request):
    todos = Todos.objects.filter(user = request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'todo/completedtasks.html', {'todos':todos})

@login_required
def viewTask(request):
    return render(request, 'todo/viewtask.html')

@login_required
def completeTask(request):
    return redirect('currenttodos')

@login_required
def deleteTask(request):
    return redirect('currenttodos')

