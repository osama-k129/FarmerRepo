from django.contrib import admin
from .models import Bid_sold, Bidded_price, BiddingProduct
# Register your models here.



admin.site.register(BiddingProduct)

admin.site.register(Bidded_price)

admin.site.register(Bid_sold)
