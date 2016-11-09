from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def area(request):
    return render(request, 'area.html')


def representations(request):
    return render(request, 'representadas.html')


def register(request):
    return render(request, 'cadastro.html')
