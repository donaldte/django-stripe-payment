from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import get_model_user
User = get_model_user()

# Create your models here.

class Products(models.Model):
    name = models.CharField(_('name of product'), max_length=100)
    price = models.IntegerField(default=0) # in cents
    description = models.TextField(default="description")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self)-> str:
        return self.name


    def get_display_price(self):
        return "{0:2f}".format(self.price / 100)    
