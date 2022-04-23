from django.db import models
from django.contrib.auth.models import User

COUNTRY_CHOICES = (
    ('0', 'Deutschland'),
    ('1', 'Belgien'),
    ('2', 'Bulgarien'),
    ('3', 'Dänemark'),
    ('4', 'Estland'),
    ('5', 'Finnland'),
    ('6', 'Frankreich'),
    ('7', 'Griechenland'),
    ('8', 'Großbritannien'),
    ('9', 'Island'),
    ('10', 'Italien'),
    ('11', 'Lettland'),
    ('12', 'Lichtenstein'),
    ('13', 'Litauen'),
    ('14', 'Luxemburg'),
    ('15', 'Niederlande'),
    ('16', 'Norwegen'),
    ('17', 'Polen'),
    ('18', 'Portugal'),
    ('19', 'Rumänien'),
    ('20', 'Schweden'),
    ('21', 'Schweiz'),
    ('22', 'Slowakei'),
    ('23', 'Spanien'),
    ('24', 'Tschechien'),
    ('25', 'Urkaine'),
    ('26', 'Ungarn'),
    ('27', 'Zypern'),
    ('28', 'Österreich'),
)


# Create your models here.
class Address(models.Model):
    customer = models.ForeignKey('customer.CustomUser', on_delete=models.CASCADE)
    street = models.CharField(max_length=255, verbose_name='Straße')
    house_no = models.CharField(max_length=12, verbose_name='Hausnummer')
    address_extra = models.CharField(max_length=255, blank=True, null=True, verbose_name='Addresszusatz')
    post_code = models.CharField(max_length=25, verbose_name='Postleitzahl')
    town = models.CharField(max_length=255, verbose_name='Stadt')
    country = models.CharField(max_length=25, choices=COUNTRY_CHOICES, default='Deutschland', verbose_name='Land')
    telephone_no = models.CharField(max_length=255, verbose_name='Telefon Nummer')
    default_shipment_address = models.BooleanField(default=False, verbose_name='Standart Lieferaddresse')
    default_billing_address = models.BooleanField(default=False, verbose_name='Standart Rechnungsaddresse')

    def __str__(self):
        return self.customer.email
