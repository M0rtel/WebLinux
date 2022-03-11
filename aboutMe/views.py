from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'aboutMe/index.html', data)

def about(request):
    return render(request, 'aboutMe/about.html')

def contacts(request):
    return render(request, 'aboutMe/contacts.html')
