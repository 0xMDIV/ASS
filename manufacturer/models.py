from django.db import models
from address.models import Address


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Hersteller Name")
    telephone_no = models.CharField(max_length=20, verbose_name="Telefon Nummer")
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name="Hersteller Adresse")
    contact_name = models.CharField(max_length=120, verbose_name="Kontakt Person")
    note = models.TextField(verbose_name="Notiz")
    status = models.BooleanField(default=False, verbose_name="aktiv/inaktiv")
