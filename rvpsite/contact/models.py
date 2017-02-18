from django.db import models
from rvpsite.contact.validators import validate_phone


class Contact(models.Model):
    name = models.CharField('nome', max_length=50)
    email = models.EmailField('email', max_length=60)
    phone = models.CharField('telefone', max_length=11, validators=[validate_phone])
    msg = models.CharField('mensagem', max_length=700)
    ipaddr = models.GenericIPAddressField('endereço IP', blank=True, null=True)
    created_at = models.DateTimeField('enviada em', auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Mensagens'
        verbose_name = 'Mensagem'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
