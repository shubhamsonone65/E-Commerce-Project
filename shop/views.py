from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact,customer,product,order
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
import random
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'home.html')

def contactquery(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        cont=contact(name=name,email=mail,Phone_No=phone,message=message)
        cont.save()
        messages.success(request, 'message sent successfully...')
    else:
        return HttpResponse('error occured...')
    return redirect('/#cont')

def userlogin(request,path):
    path='/'+path+'/'
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            nameuser=User.objects.get(email=email.lower()).username
            user=authenticate(request,username=nameuser,password=password)
        except Exception as e:
            user=None
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in successfully...')
            return redirect(path)
        else:
            messages.error(request,'Invalid Credentials...')
            return redirect(path)
    else:
        return HttpResponse('Error Occured')
def userlogin2(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            nameuser=User.objects.get(email=email.lower()).username
            user=authenticate(request,username=nameuser,password=password)
        except Exception as e:
            user=None
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in successfully...')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials...')
            return redirect('/')
    else:
        return HttpResponse('Error Occured')

def userlogout(request):
    logout(request)
    messages.success(request,'Logged out successfully...')
    return redirect('/')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        phone=request.POST.get('phone')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        acc=None
        try:
            acc=customer.objects.get(email=mail)
        except Exception as e:
            print(e)
        if acc!=None:
            messages.error(request,'account with this email already exists...')
        elif(pass1==pass2):
            user = User.objects.create_user(name,mail,pass1)
            user.save()
            cust=customer(acc=user,name=name,email=mail,phone_no=phone,pass1=pass1)
            cust.save()
            messages.success(request, 'account is successfully created...')
    else:
        return HttpResponse('error occured...')
    return redirect('/')

def prodview(request,slug):
    products={}
    if(slug=='all'):
        allproduct=product.objects.all()
        allproduct=list(allproduct)
        random.shuffle(allproduct)
    else:
        slug=slug.split('-')
        allproduct=product.objects.filter(cat=slug[1],subcat__icontains=slug[0])
        allproduct=list(allproduct)
        random.shuffle(allproduct)
    
    products={'allproduct':allproduct}
    return render(request,'prodview.html',products)

def search(request):
    products={}
    allproduct=None
    if request.method=="GET":
        search=request.GET.get('search')
        allproduct=product.objects.filter(Q(brand__icontains=search)|Q(name__icontains=search)|Q(cat__icontains=search)|Q(subcat__icontains=search))
    products={'allproduct':allproduct}
    return render(request,'prodview.html',products)

def proddetails(request,id):
    prod=product.objects.get(Proid=id)
    products={'prod':prod}
    return render(request,'proddetails.html',products)


def cart(request):    
    return render(request,'cart.html')

def buy(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.error(request,'You need to login before checkout...')
        return redirect('/cart')

    return render(request,'buy.html')

def myorder(request):
    if request.user.is_authenticated:
        orders=order.objects.filter(owner=request.user)
        return render(request,'myorders.html',{'orders':orders})
    else:
        messages.error(request,'You need to login before check orders...')
        return redirect('/')

login_required('/')
def deleteorder(request,id):
    try:
        custorder=order.objects.get(id=id)
        custorder.delete()
        messages.success(request,"order canceled...")
        return redirect('/myorders/')
    except:
        messages.error(request,"not found...")
        return redirect('/myorders/')

login_required('/')
def orderdetails(request,id):
    # try:
        custorder=order.objects.get(id=id)
        orders=json.loads(custorder.orderitem)
        total=custorder.totalprice
        custname=custorder.name.upper()
        custphone=custorder.phone
        custaddress=custorder.address+ ', City: '+custorder.city+', Zipcode: '+str(custorder.zipcode)+', State:'+custorder.state
        custdate=custorder.orderdate
        data={'orders':orders,'total':total,'name':custname,'phone':custphone,'address':custaddress,'orderdate':custdate}
        print(orders)
        return render(request,'orderdetails.html',data)
    # except:
    #     pass
        # messages.error(request,"not found...")
        # return redirect('/myorders/')

login_required('/')
def orderprod(request):
    if request.method=='POST':
        cartItem=request.POST.get('cartItems')
        total=request.POST.get('total')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('add1')+' '+request.POST.get('add2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        custorder=order(owner=request.user,orderitem=cartItem,totalprice=total,name=name,email=email,phone=phoneno,address=address,city=city,state=state,zipcode=zipcode)
        try:
            custorder.save()
            messages.success(request,'Thanks for ordering with us... You can check your orders in my orders section')
            return redirect('/')
        except:
            messages.error(request,'Something went wrong... please try again')
            return redirect('/')
        

        

