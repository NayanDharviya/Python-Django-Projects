from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.utils.http import is_safe_url
# Create your views here.
def regist(request):
    form_class=RegisterForms(request.POST or None)
    con={'req':form_class}
    if form_class.is_valid():
        # un=r.cleaned_data.get('username')
        # pwd=r.cleaned_data.get('password')
        # cpwd=r.cleaned_data.get('cpassword')
        # email=r.cleaned_data.get('email')
        user=form_class.save()
        print(user)
        con['req']=register()
        con['msg']='user created'
        return redirect('/login')
    
    return render(request,'register.html',context=con)



def login_(request):
    log=login_form(request.POST or None)
    con={'fields':log}
    #below code check that if this login page is came from something action happen or it comes directly
    #like when we click on checkout button it will check if user has login is yes that next_ is none or if not then url of checkout page is store into next_
    # this 'next' value is coming from the html page i.e. account\snippets\form.html and login.html means it is the name of input hidden field
    next_=request.GET.get('next')
    next_post=request.POST.get('next')
    redirect_path=next_ or next_post or None

    if log.is_valid():
        un=log.cleaned_data.get('fullname')
        pwd=log.cleaned_data.get('password')
        # email=log.cleaned_data.get('email')
        
        user=authenticate(request=request,username=un,password=pwd)
        if user is not None:
            
            login(request,user)
            if redirect_path:
                
                if is_safe_url(redirect_path,request.get_host()):
                    return redirect(redirect_path)

            return redirect('/home')
            
        else:
            con['next_url']=redirect_path
            con['msg']='Invalid User name or password'
           
    return render(request,'login.html',context=con)

def logoutpage(request):
    logout(request)
    return redirect('/home')