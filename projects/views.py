from unittest import installHandler
from django.shortcuts import render
from projects.models import Project
from .forms import register, newProj
from django.contrib.auth.models import User

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def index(req):
    return render(req, 'index.html', {})

def profile(req):
    return render(req, 'account.html', {})

def reg(req):
    if req.method == 'POST':
        form = register(req.POST)
        if form.is_valid():
            User.objects.create_user(form.data.get('name'), form.data.get('email'), form.data.get('password')).save()
            return render(req, 'index.html', {})
    else:
        form = register()
    return render(req, 'register_index.html', {'form': form})

def new_project(req):
    if req.method == 'POST':
        form = newProj(req.POST, req.FILES)
        if form.is_valid():
            Project(title=form.data.get('title'), description=form.data.get('description'), technology=form.data.get('technology'), image=form.data.get('image')).save()
            return render(req, 'project_index.html', {})
    else:
        form = newProj()
    return render(req, 'new_project.html', {'form': form})