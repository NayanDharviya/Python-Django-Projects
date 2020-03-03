
# This app is created for the category wise filteration of product

from django.db import models
from products.models import Product

# Create your models here.


class Tag(models.Model):
    title=models.CharField(max_length=120)
    createdDate=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    products=models.ManyToManyField(Product,blank=True)


    def __str__(self):
        return self.title