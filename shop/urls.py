from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("contact",views.contactquery,name='contact'),
    path("<path:path>/login",views.userlogin,name='userlogin'),
    path("login",views.userlogin2,name='userlogin2'),
    path("signup",views.signup,name='signup'),
    path("logout",views.userlogout,name='userlogout'),
    path("search/",views.search,name='search'),
    path("cart/",views.cart,name='cart'),
    path("cart/buy/",views.buy,name='buy'),
    path("cart/buy/order/",views.orderprod,name='order'),
    path("delete/<str:id>/",views.deleteorder,name='deleteorder'),
    path("myorders/",views.myorder,name='myorder'),
    path("myorders/orderdetails/<str:id>/",views.orderdetails,name='orderdetails'),
    path("prodview/<slug:slug>/",views.prodview,name='prodview'),
    path("proddetails/<int:id>/",views.proddetails,name='proddetails'),
]