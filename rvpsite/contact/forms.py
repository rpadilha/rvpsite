from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome ou Razão Social', max_length=50)
    email = forms.EmailField(label='Email', max_length=60)
    phone = forms.CharField(label='Telefone', max_length=11)
    msg = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'rows': 8}))
    ipaddr = forms.GenericIPAddressField(label='IP', required=False, disabled=True)