from django.shortcuts import render, redirect
from .models import Blue_todo
from .forms import TodoForm


# Create your views here.
def alltodos(request):
    tasks = Blue_todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'alltodo.html', {'tasks': tasks, 'form': form})


def Delete(request, pk):
    task = Blue_todo.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('alltodos')
    return render(request, 'delete.html', {'item': task})


def Update(request, pk):
    todo = Blue_todo.objects.get(id=pk)
    updateForm = TodoForm(instance=todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos')

    return render(request, 'update.html', {'todo': todo, 'updateForm': updateForm})
