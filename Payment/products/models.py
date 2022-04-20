from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Products(models.Model):
    name = models.CharField(_('name of product'), max_length=100)
    price = models.IntegerField(default=0) # in cents

    def __str__(self)-> str:
        return self.name


    def get_display_price(self):
        return "{0:2f}".format(self.price / 100)    