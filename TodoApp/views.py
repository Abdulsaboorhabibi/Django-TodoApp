from django.shortcuts import render

from TodoApp.forms import TodoForm
from TodoApp.models import TodoModel


def all_todo(requist):
    form = TodoForm(requist.POST)
    todos = TodoModel.objects.all()

    if requist.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        "form": form,
        "todos": todos
    }
    return render(requist, "TodoApp/All_todo.html", context)
