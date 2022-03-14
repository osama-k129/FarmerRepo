from django.db import models

from farmerapp .models import ProductTbl,Purchased
from django.contrib.auth.models import User
# Create your models here.

class BiddingProduct(models.Model):
    product = models.OneToOneField(to=ProductTbl,on_delete=models.CASCADE)
    min_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    bidding_date = models.DateField()
    bidding_start_time = models.TimeField(blank=True,null=True)
    bidding_end_time = models.TimeField(blank=True,null=True)
    complete = models.BooleanField(default=False,blank=True,null=True)


    def __str__(self):
        return self.product.product_name




class Bidded_price(models.Model):
    bid_product = models.ForeignKey(to=BiddingProduct,on_delete=models.CASCADE)
    bid_price = models.IntegerField()
    bid_date_time = models.DateTimeField(auto_now_add=True)
    bidded_by = models.ForeignKey(to=User,on_delete=models.CASCADE)


    def __str__(self):
        return self.bid_product.product.product_name + " => " +  self.bidded_by.username




class Bid_sold(models.Model):
    sold_by = models.ForeignKey(to=User,on_delete=models.CASCADE)
    bid_product = models.ForeignKey(to=Bidded_price,on_delete=models.CASCADE)
    sold_date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sold_by.username + " => " + self.bid_product.product.product_name





class Purchased_Project(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    sold_bd = models.ForeignKey(to=Bid_sold,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=300)
    paid_amount = models.FloatField()
    payment_id = models.CharField(max_length=300)
    signature_hash = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)

