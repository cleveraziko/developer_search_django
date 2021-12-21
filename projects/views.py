from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context={
        'projects': projects
    }
   
    return render(request, 'projects/project.html', context)


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    
    return render(request, 'projects/single_project.html',{
        'project': projectObj,
       
    })


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context={
        "form":form
    }
    return render(request,"projects/project_form.html", context )