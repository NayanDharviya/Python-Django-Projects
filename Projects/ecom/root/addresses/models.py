from django.db import models

# Create your models here.
from django.db import models
from billing.models import BillingProfile
# Create your models here.

#here below code is a enum type of tuple which is used for dropdown button
#where first i.e. 0th index of tuple is the value of that dropdown and 1st index define the Display purpose
ADDRESS_TYPES=(
    ('billing','Billing'),
    ('shipping','Shipping')
)


class Address(models.Model):
    billing_profile=models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    address_type=models.CharField(max_length=200,choices=ADDRESS_TYPES)
    address_line1=models.CharField(max_length=200)
    address_line2=models.CharField(max_length=200,blank=True,null=True)
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=120,default='India')
    state=models.CharField(max_length=120)
    pincode=models.CharField(max_length=20)


    def __str__(self):
        return str(self.billing_profile)
    #this function return email from the Billing_profile module  which is created in orders app because this will call __self__ function of Billing_profile module which return email field of billing_profile module

    # get_address function is used only for display 
    def get_address(self):
        return '{line1}\n{line2}\n{city}\n{state}\n{country}\n{pin}'.format(
            line1=self.address_line1,
            line2=self.address_line2 or "",
            city=self.city,
            state=self.country,
            country=self.state,
            pin=self.pincode
            )