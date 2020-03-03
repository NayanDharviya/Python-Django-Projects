from django.http import HttpResponse
from django.shortcuts import render,redirect
from carts.models import Cart

# def home_page(request):
#     return HttpResponse('<h1>new project</h1>')


    
def contact(request):
    # cont=contactpage()
    con={'field':cont}
    return render(request,'contact.html',context=con)


def home(request):
    cart_obj,new_obj=Cart.objects.new_or_get(request)
    request.session['cart_items']=cart_obj.products.all().count()
    # h=homepage()
    con={}
    if request.user.is_authenticated:
        con['name1']=request.user
    return render(request,'homepage.html',context=con)


def about(request):
    # ab=about_page()
    con={}
    return render(request,'aboutpage.html')



# def login_logout(request):
#     con={}
#     if request.user.is_authenticated:
#         con['name_']=request.user
#     return render(request,'menu.html',con)