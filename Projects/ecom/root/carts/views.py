from django.shortcuts import render,redirect    
from products.models import Product
from carts.models import Cart
from billing.models import BillingProfile
from orders.models import Order
from accounts.forms import login_form
from addresses.forms import AddressForm
from addresses.models import Address
# Create your views here.


#jsonResponse module
from django.http import JsonResponse


def cart_update(request):
    prodId=request.POST.get('pid', None)
    prod_obj=Product.objects.filter(id=prodId).first()
    cart_obj, new_obj=Cart.objects.new_or_get(request)
    
    # print(request.session.cart_id)
    # print(cart_obj)
    if prod_obj in cart_obj.products.all():
        cart_obj.products.remove(prod_obj)
    else:
        cart_obj.products.add(prod_obj)
    request.session['cart_items']=cart_obj.products.all().count()
    return redirect('cart:list')

def update_cart_api(request):
    data={}
    if request.is_ajax():
        if request.method=='POST':
            prodId=request.POST.get('pid', None)
            prod_obj=Product.objects.filter(id=prodId).first()
            cart_obj, new_obj=Cart.objects.new_or_get(request)
            if prod_obj in cart_obj.products.all():
                cart_obj.products.remove(prod_obj)
                data['added']=False
            else:
                cart_obj.products.add(prod_obj)
                data['added']=True
            
            data['cartUpdateapi']=cart_obj.products.all().count()
            request.session['cart_items']=data['cartUpdateapi']
            
    return JsonResponse(data)

def cart_home(request):
    cart_obj,new_obj=Cart.objects.new_or_get(request)
    return render(request,'carts/list.html',{'cart':cart_obj})

def cart_home_api(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    Products = []
    for prod in cart_obj.products.all():
        Products.append(
            {
                'id':prod.id,
                'detail_url':prod.get_adsolute_url(),
                'price':prod.price,
                'title':prod.pname
            }
        )
    data = {
        'products':Products,
        'subtotal':cart_obj.subtotal,
        'total':cart_obj.total
    }
    return JsonResponse(data)

    
def checkout_home(request):
    try:
        cart_obj,new_obj=Cart.objects.new_or_get(request)
        order_obj=None
        address_qs=None
        if request.user.is_authenticated:
            billingProfile_obj,bill_obj=BillingProfile.objects.new_or_get(request)
            order_obj,order_bool=Order.objects.new_or_get(billingProfile_obj,cart_obj)
            if request.session.get('shipping_address_id',None):
                order_obj.shipping_address=Address.objects.filter(id=request.session.get('shipping_address_id')).first()
                
            if request.session.get('billing_address_id',None):
                order_obj.billing_address=Address.objects.filter(id=request.session.get('billing_address_id')).first()
            order_obj.save()
            address_qs=Address.objects.filter(billing_profile=billingProfile_obj)
        if request.method=='POST':
            print(request.POST)
            if request.POST.get('razorpay_payment_id',None):
                order_obj.mark_paid()
                request.session['cart_items']=0
                del request.session['cart_id']
                del request.session['billing_address_id']
                del request.session['shipping_address_id']
                return render(request,'carts/checkout-done.html',{
                    'transid':request.POST.get('razorpay_payment_id',None)
                })
            
            #update database set status to paid
            #call checkout done page and pass 
        context={
            'order_obj':order_obj,
            'loginform':login_form(),
            'address':AddressForm(),
            'address_qs':address_qs,
        }
        
        return render(request,'carts/checkout.html',context)
    except:
        return redirect('/home')