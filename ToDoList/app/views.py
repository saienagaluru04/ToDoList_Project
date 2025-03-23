from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from app.models import *

def task_list(request):
    tasks = Task.objects.all()
    d = {'tasks': tasks}
    return render(request, 'task_list.html', d)

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
