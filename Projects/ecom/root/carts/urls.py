
from django.urls import path
from .views import *

urlpatterns = [
    path('',cart_update,name='update'),
    path('list',cart_home,name='list'),
    path('checkout',checkout_home,name='checkout'),
    path('apiupdate',update_cart_api,name='apiupdate'),
    path('apihome',cart_home_api,name='apihome')
]