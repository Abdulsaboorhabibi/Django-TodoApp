from django.urls import path
from . import  views

urlpatterns = [
    path("", views.all_todo, name="list-todo")
]