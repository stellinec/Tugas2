from django import forms
from .models import Task
class Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description",]
        labels = {'title': "Judul Task", "description": "Deskripsi Task",}