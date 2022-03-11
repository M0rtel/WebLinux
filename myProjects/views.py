from django.shortcuts import render


def my_projects(request):
    return render(request, 'myProjects/my_projects.html')

