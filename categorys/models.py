from datetime import date

from django.db import models


# Create your models here.
from product.models import Product


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateField(default=date.today())
    product = models.ForeignKey(Product)
