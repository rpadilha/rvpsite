from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def area(request):
    return render(request, 'area.html')


def representations(request):
    return render(request, 'representations.html')


def clients(request):
    return render(request, 'clients.html')

def google(request):
    return render(request, 'googleb38521f7cdc37071.html')

def newsite(request):
    return render(request, 'index2.html')