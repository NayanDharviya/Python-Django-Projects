from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView
from carts.models import Cart
# Create your views here.


#function based view
def productlistview(request):
    qs=Product.objects.all()
    con={
        'object_list':qs
    }
    return render(request,'products/list.html',con)




#class based view
class ProductListViewcbv(ListView):
    queryset=Product.objects.all()
    template_name='products/list.html'


# #function based detail view
# def productdetailview(request,pk=None):
#         product_obj=Product.objects.filter(id=pk).first()
#         con={
#             'object':product_obj
#         }

#         return render(request,'products/detail.html',con)


#class based detail view
class ProductListViewcb(DetailView):
    queryset=Product.objects.all()
    template_name='products/detail.html'

#function based detail view with auto sluh generation
def productdetailview(request,slug=None):
        product_obj=Product.objects.filter(slug=slug).first()
        cart_obj, new_obj=Cart.objects.new_or_get(request)
        con={'object':product_obj}
        if product_obj in cart_obj.products.all():
            con['in_cart']=True
        else:
            con['in_cart']=False
        
        return render(request,'products/detail.html',con)





def featuredlist(request):
    qs=Product.objects.featured()
    con={
        'object_list':qs
    }
    return render(request,'products/list.html',con)
