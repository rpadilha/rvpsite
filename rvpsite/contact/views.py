from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from rvpsite.contact.forms import ContactForm
from rvpsite.contact.models import Contact


def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contacts/contact_form.html', {'form': form })

    _get_ip_address(request, form.cleaned_data)

    Contact.objects.create(**form.cleaned_data)

    _send_mail('Nova mensagem do site',
               form.cleaned_data['email'],
               'rvprepresentacao@gmail.com',
               #'tonare@gmail.com',
               'contacts/contact_email.txt',
               form.cleaned_data)

    messages.success(request, 'Mensagem enviada com sucesso!')
    return HttpResponseRedirect('/contato/')


def new (request):
    return render(request, 'contacts/contact_form.html',
                  {'form': ContactForm()})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [to])


def _get_ip_address(request, context):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        context['ipaddr'] = x_forwarded_for.split(',')[-1]
    else:
        context['ipaddr'] = request.META.get('REMOTE_ADDR')
