from django.shortcuts import render
from django.views.generic import TemplateView



def home(request, template_name='home.html'):
    return render(request, template_name)


def todo_list(request):
    pass

def todo_view(request):
    pass

def todo_create(request):
    pass

def todo_update(request):
    pass

def todo_delete(request):
    pass
