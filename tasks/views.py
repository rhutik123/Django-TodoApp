from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = addTask()

    if request.method == 'POST':
        form = addTask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/index.html', context)

def update(request, pk):
    tasks = Task.objects.get(id=pk)
    form = addTask(instance=tasks)

    if request.method == 'POST':
        form = addTask(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'tasks/update.html', context)

def delete(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)