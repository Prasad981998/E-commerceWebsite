from django.shortcuts import render
from django.views import View
from .models import Product,Customer,Cart,OrderPlaced

class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(catagory='TW')
        bottomwears=Product.objects.filter(catagory='BW')
        mobiles=Product.objects.filter(catagory='M')
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles})
#def home(request):
# return render(request, 'app/home.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})
#def product_detail(request):
# return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobile=Product.objects.filter(catagory='M')
    elif data=='samsung' or data=='Apple':
        mobile=Product.objects.filter(catagory='M').filter(brand=data)
    return render(request, 'app/mobile.html',{'mobile':mobile})

def topwear(request,data=None):
    if data==None:
        topwear=Product.objects.filter(catagory='TW')
    elif data=='benblue' or data=='cooper' or data=='zudio':
        topwear=Product.objects.filter(catagory='TW').filter(brand=data)
    return render(request,'app/topwear.html',{'topwear':topwear})


def bottomwear(request,data=None):
    if data==None:
        bottomwear=Product.objects.filter(catagory='BW')
    elif data=='cooper' or data=='Lee':
        bottomwear=Product.objects.filter(catagory='BW').filter(brand=data)
    return render(request,'app/bottomwear.html',{'bottomwear':bottomwear})


def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
