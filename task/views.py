from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import Task

def add_task(req) :
    if req.method == 'POST' :
        task_form = TaskForm(req.POST)
        if task_form.is_valid() :
            task_form.save()
            return redirect('show_task')
        
    task_form = TaskForm()
    return render(req, 'task/add_task.html', {'form' : task_form})


def edit_task(req, id) :
    task = Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if req.method == 'POST' :
        task_form = TaskForm(req.POST, instance=task)
        if task_form.is_valid() :
            task_form.save()
            return redirect('show_task')
        
    return render(req, 'task/add_task.html', {'form' : task_form})


def delete_task(req, id) :
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')


def show_task(req) :
    data = Task.objects.all()
    return render(req, 'task/show_task.html', {'data' : data})
