from django.db import models

from manufacturer.models import Manufacturer

COLOR_CHOICES = (
    ('RED', 'Rot'),
    ('RED', 'Blau'),
    ('RED', 'Grün'),
    ('UNKNOWN', 'Unbekannt'),
)

MATERIAL_CHOICES = (
    ('STONE', 'Stein'),
    ('WOOD', 'Holz'),
    ('PLASTIC', 'Plastik'),
    ('EDELSTAHL', 'Edelstahl'),
    ('GLASS', 'Glas'),
    ('UNKNWON', 'Unbekannt'),
)


class Product(models.Model):
    product_name = models.CharField(max_length=255, default="", verbose_name="Produkt Name")
    description = models.TextField(verbose_name="Produkt Beschreibung", blank=True, null=True)
    material = models.CharField(choices=MATERIAL_CHOICES, default='Unknown')
    quantity = models.PositiveIntegerField(verbose_name="Anzahl", default=0)
    price_without_taxes = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Preis (ohne Steuern)")
    price_with_taxes = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,
                                           verbose_name="Preis (mit Steuern)")
    weight = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True, verbose_name="Produkt Gewicht")
    delivery_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                        verbose_name="Versandkosten")
    article_no = models.CharField(unique=True, max_length=35, verbose_name="Artikelnummer")
    manufacturer_order_no = models.CharField(unique=True, max_length=35, blank=True, null=True,
                                             verbose_name="Hersteller Artikelnummer")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name="Hersteller")
    color = models.CharField(choices=COLOR_CHOICES, default='Unknown', verbose_name="Produkt Farbe")
    discount_possible = models.BooleanField(default=False, verbose_name="Kann Rabattiert werden")
    ranking = models.IntegerField(null=True, blank=True, verbose_name="Ranking")
    can_be_gifted = models.BooleanField(default=False, verbose_name="Kann verschenkt werden")

    def check_quantity(self):
        # check for quantity if < 15 alert, needs to be reordered
        pass
