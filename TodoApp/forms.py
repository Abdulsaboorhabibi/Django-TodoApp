from django import forms

from TodoApp.models import TodoModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = "__all__"
        widgets = {
            'task': forms.TextInput(
                attrs={
                    'class': 'flex-1 border-3 border-gray-800 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6',
                    "placeholder": "Enter your name here...."
                }
            )
        }
