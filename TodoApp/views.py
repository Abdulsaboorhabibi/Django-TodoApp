from django.shortcuts import render


def all_todo(requist):
    form = ""
    todos = ""
    context = {
        "form": form,
        "todos": todos
    }
    return render(requist, "TodoApp/All_todo.html", context)
