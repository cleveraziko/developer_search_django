from django.shortcuts import render

# Create your views here.

def projects(request):
    msg = 'hello'
    return render(request, 'projects/project.html', {'msg':msg})


def project(request,pk):
    return render(request, 'projects/single_project.html')
