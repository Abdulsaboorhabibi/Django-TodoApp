from django.shortcuts import render

from TodoApp.forms import TodoForm
from TodoApp.models import TodoModel


def all_todo(requist):
    form = TodoForm(requist.POST)
    todos = TodoModel.objects.all()

    if requist.method == 'POST':
        if form.is_valid():
            form.save()

    context = {"form": form, "todos": todos}
    return render(requist, "TodoApp/All_todo.html", context)


def Edit_Todo(requist, slug):
    todo_to_edit = TodoModel.objects.get(slug=slug)
    edit_model = TodoModel(slug=slug)
    if requist.method == "POST":
        edit_model.task = requist.GET("task")
        edit_model.is_done = requist.GET("is_done")
        edit_model.slug = requist.GET("slug")
        edit_model.save()

    context = {"Edit_todo": todo_to_edit }
    return render(requist, "TodoApp/Edit_todo.html", context)
