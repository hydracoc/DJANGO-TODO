from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ name)
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'taskmaster/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password in incorrect')
            return render(request, 'taskmaster/login.html')
    else:
        return render(request, 'taskmaster/login.html')

def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')     # This ensures that only logged in users are allowed to be in this page
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskmaster/taskmaster.html', {'tasks': tasks})

@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        task_content = request.POST.get('task')
        if task_content:
            new_task = Task(description=task_content, user=request.user)
            new_task.save()
        return redirect('home')
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskmaster/taskmaster.html', {'tasks': tasks})


@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return redirect('home')

@login_required(login_url='login')
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task_description = request.POST.get('description')
        if task_description:
            task.description = task_description
            task.save()
            return redirect('home')
    return redirect('home')

@login_required(login_url='login')
def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.completed = True
        task.save()
        return redirect('home')
    return redirect('home')