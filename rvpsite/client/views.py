from django.shortcuts import render
from rvpsite.client.forms import LoginForm


def clients(request):
    return render(request, 'clients/clients.html')


def clients_tmp(request):
    return render(request, 'clients/clients_form.html', {'form' : LoginForm()})
