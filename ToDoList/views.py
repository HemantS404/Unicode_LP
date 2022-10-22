from django.shortcuts import render, redirect
from ToDoList.models import task
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm, Image

def index(request):
    a = task.objects.filter(user = request.user)
    dict1 = a.values()
    for i in dict1:
        if i['complete'] == False:
            i['complete'] = 'INCOMPLETE'
        else:
            i['complete'] = 'COMPLETE'
    return render(request, 'Todo.html', context = {'data' : dict1})

def details(request, id):
    a = task.objects.get(id = id)
    if a.complete == False:
        a.complete = 'INCOMPLETE'
    else:
        a.complete = 'COMPLETE'
    return render(request, 'details.html', context = {'data' : a})

def delete(request, id):
    a = task.objects.get(id = id)
    a.delete()
    return render(request, 'giver.html', {'message': 'DATA DELETED'})

def update(request, id):
    a = task.objects.get(id = id)
    a.complete = True
    a.save()
    return render(request, 'giver.html', {'message': 'DATA UPDATED'})


def create(request):
    if request.method == 'GET':
        context = {}
        context['form'] = Image()
        return render(request, 'create.html', context)
    elif request.method == 'POST':
        form = Image(request.POST, request.FILES)
        if form.is_valid():
            a = task(
                user = request.user,
                title = request.POST['title'],
                description = request.POST['description'],
                create = datetime.now(),
                image = form.cleaned_data["image"]
                )
            a.save()
        return render(request, 'create.html', context = {'m1':'DATA STORED', 'm2':'FILL THE FORM AGAIN TO ADD ANOTHER TASK', 'form' : Image()})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Username OR Password do not exsits ...."))	
            return redirect('login')
    else:
        return render(request, 'login.html')

def signup_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form':form,})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('login')