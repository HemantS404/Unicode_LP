from django.shortcuts import render, redirect
from .models import task
from datetime import datetime
from .forms import priorityForm

def mainpage(request):
    a = task.objects.filter(user = request.user)
    dict1 = a.values()
    for i in dict1:
        if i['complete'] == False:
            i['complete'] = 'INCOMPLETE'
        else:
            i['complete'] = 'COMPLETE'
    return render(request, 'task_handler/Todo.html', context = {'data' : dict1, 'user': request.user})

def details(request, id):
    a = task.objects.get(id = id)
    if a.complete == False:
        a.complete = 'INCOMPLETE'
    else:
        a.complete = 'COMPLETE'
    return render(request, 'task_handler/details.html', context = {'data' : a})

def delete(request, id):
    a = task.objects.get(id = id)
    a.delete()
    return render(request, 'task_handler/giver.html', {'message': 'DATA DELETED'})

def update(request, id):
    a = task.objects.get(id = id)
    a.complete = True
    a.save()
    return render(request, 'task_handler/giver.html', {'message': 'DATA UPDATED'})


def create(request):
    if request.method == 'GET':
        form = priorityForm()
        return render(request, 'task_handler/create.html', {'form': form})
    elif request.method == 'POST':
        form = priorityForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['priority']
        a = task(
                user = request.user,
                title = request.POST['title'],
                priority = f,
                description = request.POST['description'],
                create = datetime.now()
            )
        a.save()
        return render(request, 'task_handler/create.html', context = {'m1':'DATA STORED', 'm2':'FILL THE FORM AGAIN TO ADD ANOTHER TASK','form': form})

