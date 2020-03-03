from .views import *
from django.urls import path

urlpatterns = [
    path('create',checkout_address_create_view,name='create'),
    path('reuse',checkout_address_reuse_view,name='reuse'),
   
]