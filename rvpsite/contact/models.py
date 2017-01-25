from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=11)
    msg = models.CharField(max_length=700)
    ipaddr = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
