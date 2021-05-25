from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    Phone_No=models.IntegerField(default=None)
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class customer(models.Model):
    acc=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone_no=models.IntegerField(default=None)
    pass1=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class product(models.Model):
    category=[('Shirts','Shirts'),('Jeans','Jeans'),('Jackets','Jackets'),('Gymwear','Gymwear'),('Blazers','Blazers'),('Shoes','Shoes')]
    subcategory=[('CasualShirts','Casual Shirt'),('FormalShirts','Formal Shirt'),('Skinny','Skinny'),('Regular','Regular'),('Slim','Slim'),('CasualShoes','Casual Shoes'),('SportShoes','Sport Shoes'),('FormalShoes','Formal Shoes')]
    Proid=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    cat=models.CharField(choices=category,max_length=7)
    subcat=models.CharField(choices=subcategory,max_length=12)
    desc=models.TextField(max_length=300)
    price=models.IntegerField()
    image=models.ImageField(upload_to='IMG/products/')

    def __str__(self):
        return self.brand+' '+self.name


class order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    orderitem=models.TextField(null=False)
    totalprice=models.CharField(max_length=500)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    address=models.TextField(max_length=300)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    orderdate=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name.upper()+' Order: Id- '+ str(self.id)

