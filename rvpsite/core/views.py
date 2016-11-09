from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def area(request):
    return render(request, 'area.html')


def representations(request):
    return render(request, 'representations.html')


def register(request):
    return render(request, 'register.html')
