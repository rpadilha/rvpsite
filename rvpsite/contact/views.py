from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from rvpsite.contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                form.cleaned_data['ipaddr'] = x_forwarded_for.split(',')[-1]
            else:
                form.cleaned_data['ipaddr'] = request.META.get('REMOTE_ADDR')

            body = render_to_string('contacts/contact_email.txt', form.cleaned_data)

            mail.send_mail('Nova mensagem do site',
                           body,
                           form.cleaned_data['email'],
                           ['rvprepresentacao@gmail.com'])

            messages.success(request, 'Mensagem enviada com sucesso!')
            return HttpResponseRedirect('/contato/')

        else:
            return render(request, 'contacts/contact_form.html', {'form': form })

    else:
        context = {'form': ContactForm()}
        return render(request, 'contacts/contact_form.html', context)
