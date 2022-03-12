from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_projects, name='my_projects'),
    path('<int:pk>', views.ProjectsDetailView.as_view(), name='projects-detail') #когда мы обращаемся к классу нужно добавлять as_view()
]
