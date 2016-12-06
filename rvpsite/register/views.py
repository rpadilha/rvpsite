from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from rvpsite.register.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            body = render_to_string('registers/register_email.html', form.data)

            mail.content_type ='html'
            mail.send_mail('RVP Representação - Confirmação de Cadastro',
                           body,
                           'rvprepresentacao@gmail.com',
                           ['tonare@gmail.com', form.cleaned_data['email']])
            messages.success(request, 'Cadastro realizado com sucesso!')
            messages.success(request, 'Você receberá um e-mail em breve.')
            return HttpResponseRedirect('/cadastro/')

        else:
            return render(request, 'registers/register_form.html', {'form': form})

    else:
        context = {'form': RegisterForm()}
        return render(request, 'registers/register_form.html', context)

