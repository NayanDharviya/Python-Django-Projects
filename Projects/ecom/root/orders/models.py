from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from carts.models import Cart
from billing.models import BillingProfile
from addresses.models import Address
from django.db.models.signals import pre_save,post_save
from decimal import Decimal
from products.utils import unique_order_id

# Create your models here.
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)
class OrderManager(models.Manager):
    def new_or_get(self,billing_profile,cart_obj):
        created=False
        qs=self.get_queryset().filter(
            billing_profile=billing_profile,
            cart=cart_obj,
            status='created'
        )
        print('order Manager qs=',qs)
        if qs.count==1:
            obj=qs.first()
        else:
            obj=self.model.objects.create(
                billing_profile=billing_profile,
                cart=cart_obj
                )
            created=True
        return obj,created

class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True) #ASFGHH3345678SDFGHJK
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.CASCADE)
    shipping_address= models.ForeignKey(Address, related_name="shipping_address",null=True, blank=True, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, default='created', choices=ORDER_STATUS_CHOICES)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) 
    total = models.DecimalField(max_digits=8, decimal_places=2,default=0.0)  #GST

    objects=OrderManager()

    def __str__(self): 
        return self.order_id

    def update_total(self):
        self.order_total=self.cart.total
        self.total=round(self.cart.total * Decimal(1.08),2)

    def check_done(self):
        if self.billing_address and self.billing_profile and self.shipping_address and self.total >0:
            return True
        return False
    
    def mark_paid(self):
        if self.check_done():
            self.status='paid'
            self.save()
        return self.status
    
def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id=unique_order_id(instance)

pre_save.connect(pre_save_create_order_id,sender=Order)

def post_save_order(sender,instance,created,*args,**kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order,sender=Order)

def post_save_cart_total(sender,instance,created,*args,**kwargs):
    if not created:
        cart_obj=instance
        cart_id=cart_obj.id
        qs=Order.objects.filter(cart__id=cart_id)
        if qs.count()==1:
            order_obj=qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total,sender=Cart)