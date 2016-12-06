from django import forms

class RegisterForm(forms.Form):

    cities = (
        ('null', 35*'-'),
        ('Aperibé','Aperibé'),
        ('Bom Jesus do Itabapoana','Bom Jesus do Itabapoana'),
        ('Cambuci','Cambuci'),
        ('Campos dos Goytacazes','Campos dos Goytacazes'),
        ('Cardoso Moreira','Cardoso Moreira'),
        ('Itaocara','Itaocara'),
        ('Itaperuna','Itaperuna'),
        ('Italva','Italva'),
        ('Laje do Muriaé','Laje do Muriaé'),
        ('Miracema','Miracema'),
        ('Natividade','Natividade'),
        ('Porciúncula','Porciúncula'),
        ('Santo Antonio de Pádua','Santo Antonio de Pádua',),
        ('São Fidélis','São Fidélis'),
        ('São Francisco do Itabapoana','São Francisco do Itabapoana'),
        ('São João da Barra','São João da Barra'),
        ('Varre-Sai','Varre-Sai'),
    )

    states = (
        ('null', 35*'-'),
        ('Rio de Janeiro','Rio de Janeiro'),
    )

    name = forms.CharField(label='Nome da Empresa')
    cnpj = forms.CharField(label='CNPJ', help_text='Texto de Ajuda do Campo')
    insc_estadual = forms.CharField(label='Inscrição Estadual')
    phone = forms.CharField(label='Telefone')
    email = forms.EmailField(label='E-mail')
    contact_person = forms.CharField(label='Pessoa de Contato')
    address = forms.CharField(label='Endereço')
    neighborhood = forms.CharField(label='Bairro')
    city = forms.ChoiceField(choices=cities, label='Cidade')
    state = forms.ChoiceField(choices=states, label='Estado')
    zip = forms.CharField(label='CEP')

    def clean_city(self):
        if self.cleaned_data['city'] == 'null':
            raise forms.ValidationError("Este campo é obrigatório.")

    def clean_state(self):
        if self.cleaned_data['state'] == 'null':
            raise forms.ValidationError("Este campo é obrigatório.")
