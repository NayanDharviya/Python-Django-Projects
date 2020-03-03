from django import forms
from .models import *

class AddressForm(forms.ModelForm):
    class Meta: 
        #this Meta class is built in class which provides to create user defined form from model field
        model=Address
        #this fields is the inherit from the .model and this field is defined which we want to display on the modelform
        fields=[
            'address_line1',
            'address_line2',
            'city',
            'country',
            'state',
            'pincode'
        ]

        widgets={
            'address_line1':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'address_line2':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter city'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter country'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter state'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Pincode'})


        }