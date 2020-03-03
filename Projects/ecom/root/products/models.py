from django.db import models
from django.urls import reverse
from .utils import *
from django.db.models.signals import pre_save,post_save
from django.db.models import Q



class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

# class FeaturedQuerySet(models.query.QuerySet):
    def featured_active(self):
        return self.filter(active=True,featured=True)
    
    def search(self,query):
        lookups=(Q(pname__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(tag__title__icontains=query))
        return self.filter(lookups).distinct() 

    
    
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    def all(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured_active()

    def search(self,query):
        return self.get_queryset().search(query)
   


# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=100)
    slug=models.SlugField(null=True,unique=True,blank=True)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=6)
    createdate=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(blank=True,null=True)
    quantity=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    featured=models.BooleanField()

    objects=ProductManager()
    
    def __str__(self):
        return self.pname


    def get_adsolute_url(self):
        return reverse('products:detail',kwargs={'slug':self.slug})


def product_pre_save_receiver(sender,instance,*args,**kwargs):
        instance.slug=unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=Product)
    

    
