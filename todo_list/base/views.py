from asyncio import Task
from typing import List
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

