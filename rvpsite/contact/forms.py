from django import forms
from rvpsite.contact.models import Contact


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
