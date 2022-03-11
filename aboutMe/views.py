from django.shortcuts import render

def index(request):
    return render(request, 'aboutMe/index.html')

def about(request):
    return render(request, 'aboutMe/about.html')
