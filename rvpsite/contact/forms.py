from django import forms

from rvpsite.contact.models import Contact
from rvpsite.contact.validators import validate_phone


class ContactFormOld(forms.Form):
    name = forms.CharField(label='Nome ou Razão Social', max_length=50)
    email = forms.EmailField(label='Email', max_length=60)
    phone = forms.CharField(label='Telefone', max_length=11, validators=[validate_phone])
    msg = forms.CharField(label='Mensagem', max_length=700, widget=forms.Textarea(attrs={'rows': 8}))
    ipaddr = forms.GenericIPAddressField(label='IP', required=False, disabled=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return " ".join(words)

    def clean_email(self):
        email = self.cleaned_data['email']
        words = [w.lower() for w in email.split()]
        return " ".join(words)

    def clean_msg(self):
        msg = self.cleaned_data['msg']
        words = [w.lower() for w in msg.split()]
        return " ".join(words)


class ContactForm(forms.ModelForm):
    msg = forms.CharField(label='Mensagem', max_length=700, widget=forms.Textarea(attrs={'rows': 8}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'msg', 'ipaddr']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return " ".join(words)

    def clean_email(self):
        email = self.cleaned_data['email']
        words = [w.lower() for w in email.split()]
        return " ".join(words)

    def clean_msg(self):
        msg = self.cleaned_data['msg']
        words = [w.lower() for w in msg.split()]
        return " ".join(words)
