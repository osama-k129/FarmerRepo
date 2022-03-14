from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField





class User_profile(models.Model):
    user = OneToOneField(to=User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=True,null=True)
    address = models.CharField(max_length=300,blank=True,null=True)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    photo = models.FileField(upload_to="profile_photo",blank=True,null=True)
    farmer_approved = models.BooleanField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return self.user.username



class Product_catagory(models.Model):
    catagory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory_name



class ProductTbl(models.Model):
    select_catagory = models.ForeignKey(to=Product_catagory,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200,blank=True,null=True)
    product_quantity = models.CharField(max_length=200,blank=True,null=True)
    product_price = models.CharField(max_length=200,blank=True,null=True)
    product_about = models.TextField(blank=True,null=True)
    product_photo = models.FileField(upload_to="product_images")
    upload_by = models.ForeignKey(to=User_profile,on_delete=models.CASCADE,blank=True,null=True)
    sold = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name



class Purchased(models.Model):
    select_product = models.ForeignKey(to=ProductTbl,on_delete=models.CASCADE)
    seller = models.ForeignKey(to=User_profile,on_delete=models.CASCADE)
    buyer = models.ForeignKey(to=User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    accept = models.BooleanField(blank=True,null=True)
    reject = models.BooleanField(default=False)
    



class ContactTbl(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=300)



class SampleImages(models.Model):
    photo = models.FileField(upload_to="sample")

    

