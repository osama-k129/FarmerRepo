from django.contrib import admin

# Register your models here.

from .models import ContactTbl, ProductTbl, Product_catagory, Purchased, SampleImages, User_profile



admin.site.register(User_profile)


admin.site.register(ProductTbl)


admin.site.register(Product_catagory)
admin.site.register(Purchased)
admin.site.register(ContactTbl)
admin.site.register(SampleImages)