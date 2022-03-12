from django.shortcuts import render
from .models import Projects
from django.views.generic import DetailView

def my_projects(request):
    projects = Projects.objects.order_by('title')                                  # Первый способ получений данный через функцию
    return render(request, 'myProjects/my_projects.html', {'projects': projects})


class ProjectsDetailView(DetailView):                                              # Второй способ получений данный через класс
    model = Projects
    template_name = 'myProjects/details_view.html'
    context_object_name = 'projects'

