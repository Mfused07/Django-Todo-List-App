# forms represnetation of model
from django import forms
from django.forms import ModelForm

from .models import *


# class meta need 2 values of minimal 1- which model are u tryn to create form for 2- what field to allow
# need to import dis form in views
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'