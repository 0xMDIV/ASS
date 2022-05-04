from django.db import models

# Create your models here.
from customer.models import CustomUser


class Coupon(models.Model):
    name = models.CharField(max_length=15, verbose_name="Coupon Code")
    discount_percent = models.IntegerField(verbose_name="Rabatt in %")
    active = models.BooleanField(default=False, verbose_name="aktiv/Inaktiv")
    created_at = models.DateTimeField(verbose_name="Erstellungsdatum")
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name="Ersteller")
