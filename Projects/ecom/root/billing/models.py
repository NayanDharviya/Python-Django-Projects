from django.db import models
from django.conf import settings
from django.db.models.signals import post_save,pre_save

User=settings.AUTH_USER_MODEL

import razorpay
# here we are using razorpay api function directly by using python library or we can usr api key for this use like we have to define json response and then we can make changes in it
client=razorpay.Client(auth=('rzp_test_RzzrQOs3bwXsky','mTm7wXdarHd7sLXWRCQWJCC3'))


# Create your models here.
class BillingProfileManager(models.Manager):
        def new_or_get(self,request):
                obj=None
                user=request.user
                created=False
                if user.is_authenticated:
                        obj,created=self.model.objects.get_or_create(user=user,email=user.email)
                return obj,created



class BillingProfile(models.Model):
        user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
        email=models.EmailField()
        active=models.BooleanField(default=True)
        update=models.DateTimeField(auto_now=True)
        timestamp=models.DateTimeField(auto_now_add=True)
        customer_id=models.CharField(max_length=120,null=True,blank=True)

        objects=BillingProfileManager()
        def __str__(self):
                return self.email


def user_created_receiver(sender,instance,created,*args,**kwargs):
        if created and instance.email:
                BillingProfile.objects.get_or_create(user=instance,email=instance.email)

post_save.connect(user_created_receiver,sender=User)

def billing_profile_created_receiver(sender,instance,*args,**kwargs):
        if not instance.customer_id and instance.email:
                print('ACTUAL API REQUEST SEND TO RAZORPAY')
                name=instance.user.full_name
                mobile=instance.user.mobile
                customer=client.customer.create(data={
                        'name':name,
                        'email':instance.email,
                        'contact':mobile
                })
                print(customer,customer.get('id'))
                instance.customer_id=customer.get('id')

pre_save.connect(billing_profile_created_receiver,sender=BillingProfile)
