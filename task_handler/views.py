from pkgutil import get_data
from django.shortcuts import render, redirect
from .models import task
from datetime import datetime
from .forms import priorityForm
from django.contrib.auth.decorators import login_required

@login_required
def mainpage(request):
    dict1 = task.get_tuples(_user = request.user)
    for i in dict1:
        if i['complete'] == False:
            i['complete'] = 'INCOMPLETE'
        else:
            i['complete'] = 'COMPLETE'
    for i in dict1:
        if i['priority'] == '1':
            i['priority'] = 'Urgent & Important'
        elif i['priority'] == '2':
            i['priority'] = 'Urgent & Not Important'
        elif i['priority'] == '3':
            i['priority'] = 'Not Urgent & Important'
        elif i['priority'] == '4':
            i['priority'] = 'Not Urgent & Not Important'
    return render(request, 'task_handler/Todo.html', context = {'data' : dict1, 'user': request.user})

@login_required
def details(request, id):
    a = task.get_tuples(_id =id)
    if a.complete == False:
        a.complete = 'INCOMPLETE'
    else:
        a.complete = 'COMPLETE'
    if a.priority == '1':
        a.priority = 'Urgent & Important'
    elif a.priority == '2':
        a.priority = 'Urgent & Not Important'
    elif a.priority == '3':
        a.priority = 'Not Urgent & Important'
    elif a.priority == '4':
        a.priority = 'Not Urgent & Not Important'
    return render(request, 'task_handler/details.html', context = {'data' : a})

@login_required
def delete(request, id):
    a = task.get_tuples(_id =id)
    a.delete()
    return render(request, 'task_handler/giver.html', {'message': 'DATA DELETED'})

@login_required
def update(request, id):
    a = task.get_tuples(_id =id)
    a.complete = True
    a.save()
    return render(request, 'task_handler/giver.html', {'message': 'DATA UPDATED'})

@login_required
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

