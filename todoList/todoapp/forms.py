from django import forms
from .models import Blue_todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Blue_todo
        fields = ['task', ]
