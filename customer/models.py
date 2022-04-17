from django.db import models


GENDER_CHOICES = {
    ('M', 'Herr'),
    ('F', 'Frau'),
}
# # Create your models here.
# class Customer(models.Model):
#
#     salutation = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nachname')
#     first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Vorname')
#     mail = models.CharField