from django.shortcuts import render, redirect
from .forms import TaskForm, UpdateTaskForm
from .models import Task


# Create your views here.


def home(request):
    context = {'success': True, 'name': 'Simeon'}
    if request.method == "POST":
        # Handle the form here
        title = request.POST['title']
        desc = request.POST['desc']
        complete_task = Task.objects.filter(complete=True)
        # print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True,
                   'complete_task': complete_task,
                   'form': TaskForm}
    return render(request, "index.html", context)


def tasks(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    context = {'tasks': allTasks}
    return render(request, "tasks.html", context)


def Update(request, pk):
    task = Task.objects.get(id=pk)
    updateForm = UpdateTaskForm(instance=task)
    if request.method == 'POST':
        updateForm = UpdateTaskForm(request.POST, instance=task)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('tasks')

    return render(request, 'update.html', {'updateForm': updateForm, })


def Delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'delete.html', {'item': task, })


def CompleteTask(request, pk):
    task = Task.objects.get(id=pk)
    complete_task = Task.objects.filter(complete=True)
    if request.method == 'POST':
        form = TaskForm
        if complete_task == Task.objects.filter(complete=True):
            form.save()
            return redirect('tasks')

    return render(request, 'complete.html', {'form': form, })



