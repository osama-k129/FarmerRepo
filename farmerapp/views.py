from django.http.response import JsonResponse
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from .models import *
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def Base(request):
    return render(request, 'farmerapp/base.html')

def Loginpage(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        user_type = request.POST['usertype']

        if password1 ==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('loginpage')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email-id already taken")
                return redirect('loginpage')
            else:
                if user_type == 'farmer':
                    user = User.objects.create_user(username=username,email=email,password = password1,is_staff=True)
                else:
                    user = User.objects.create_user(username=username,email=email,password = password1)
                if user is not None:
                    auth.login(request,user)
                    return redirect("index")
                   
                return redirect('loginpage')
        else:
            return redirect('loginpage')
    else:
        return render(request, 'farmerapp/login.html')

    





def Index(request):
    product = ProductTbl.objects.all()[:4:-1]
    context = {
        'product' : product
    }
    return render(request,'farmerapp/index.html',context)





def Sign_in(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            if(user.is_staff):
                return redirect('index')
            else:
                return redirect('index')
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect("loginpage")
    else:    
        return redirect('loginpage')





def Logout(request):
    auth.logout(request)
    return redirect("loginpage")





def About(request):
    return render(request,'farmerapp/about.html')



def Contact(request):
    return render(request,'farmerapp/contact.html')





def Catagory(request,myid):
    cat = Product_catagory.objects.all()
    ca = Product_catagory.objects.get(id = myid)
    products = ProductTbl.objects.filter(select_catagory = ca)

    context = {
        'cat' : cat,
        'products' : products
    }
    return render(request,'adminapp/catagory.html',context)




def Our_product(request):
    cat = Product_catagory.objects.all()
    products = ProductTbl.objects.all()

    context = {
        'cat' : cat,
        'products' : products
    }
    return render(request,'farmerapp/our-product.html',context)





def Admin_base(request):
    return render(request,'adminapp/admin-base.html')




def Product_detail(request,myid):
    product = ProductTbl.objects.get(id = myid)
    context = {
        'product' : product
    }
    return render(request,'farmerapp/product-detail.html',context)




@login_required(login_url='loginpage')
def Dashboard(request):
    user = request.user
    if user.is_staff:
        total_product = ProductTbl.objects.filter(upload_by = user.user_profile).count()
        total_product_sell = Purchased.objects.filter(seller = user.user_profile).count()
        total_profitt = Purchased.objects.filter(seller = user.user_profile,accept=True)
        total_profit = 0
        for i in total_profitt:
            total_profit = total_profit + int(i.select_product.product_price)
        print(total_profit)

        pur = Purchased.objects.filter(seller = user.user_profile)[:10:-1]
        
        context = {
            'total_profit' : total_profit,
            'total_product' : total_product,
            'total_product_sale' : total_product_sell,
            'pur' : pur,
        }
        return render(request,'adminapp/dashboard.html',context)
    else:
        return HttpResponse("Your are not former")



@login_required(login_url='loginpage')
def Add_product(request):
    try:
        user = request.user
        if user.is_staff:
            if request.method == "POST":
                cat = request.POST['select_catagory']
                name = request.POST['product_name']
                quantity = request.POST['product_quantity']
                price = request.POST['product_price']
                photo = request.FILES['product_photo']
                about = request.POST['about_product']
                catt = Product_catagory.objects.get(id = cat)
                pro = ProductTbl(select_catagory = catt,product_name = name,product_quantity=quantity,product_price=price,product_about=about,product_photo=photo,upload_by = user.user_profile)
                pro.save()
                messages.info(request,"Product added successfully")
                return redirect('add-product')
            else:
                cata = Product_catagory.objects.all()
                context = {
                    'cat': cata
                }

                return render(request,'adminapp/add-product.html',context)
        else:
            return HttpResponse("You are not Farmer")
    except:
        cata = Product_catagory.objects.all()
        context = {
            'cat': cata
        }
        return render(request,'adminapp/add-product.html',context)




@login_required(login_url='loginpage')
def Product_list(request):
    user = request.user
    if user.is_staff:
        products = ProductTbl.objects.filter(upload_by = user.user_profile)
        context = {
            'products' : products
        }
        return render(request,'adminapp/product-list.html',context)
    else:
        return HttpResponse("you are not former")





@login_required(login_url='loginpage')
def Delete_product(request,myid):
    user = request.user
    if user.is_staff:
        pro = ProductTbl.objects.get(id = myid)
        pro.delete()
        messages.info(request, 'Product deleted successfully')

        return redirect('product-list')
    else:
        return HttpResponse("Your are not former")



@login_required(login_url='loginpage')
def Edit_product(request,myid):
    if request.method == "POST":
        pro = ProductTbl.objects.get(id = myid)
        pro.product_name = request.POST['product_name']
        pro.product_quantity= request.POST['product_quantity']
        pro.product_price = request.POST['product_price']
        pro.product_about = request.POST['about_product']
        try:
            pro.product_photo = request.FILES['product_photo']
            pro.save()
        except:
            pro.save()
        messages.info(request, 'Product Updated  successfully')
        return redirect('product-list')
    else:
        product = ProductTbl.objects.get(id = myid)
        context = {
            'product' : product
        }
        return render(request,'adminapp/edit-product.html',context)




@login_required(login_url='loginpage')
def Sales_report(request):
    user = request.user
    if user.is_staff:
        pur = Purchased.objects.filter(seller = user.user_profile ,accept = True)
        context = {
            'pur' : pur
        }
        return render(request,'adminapp/sales-report.html',context)
    else:
        return HttpResponse("You are not former")




@login_required(login_url='loginpage')
def Orders(request):
    user = request.user
    if user.is_staff:
        pur = Purchased.objects.filter(seller = user.user_profile)
        context = {
            'pur' : pur
        }
        return render(request,'adminapp/orders.html',context)
    else:
        return HttpResponse("your are not former")


@login_required(login_url='loginpage')
def Profile(request):
    userr = request.user
    user_profile = get_object_or_404(User_profile, user=userr)  
    context={
        'user_profile' : user_profile
    }
    return render(request,'adminapp/profile.html')





@login_required(login_url='loginpage')
def Edit_profile(request):
    user = request.user
    # if user.is_staff:
    if request.method == "POST":
        user_profile = get_object_or_404(User_profile, user=user)  
        user_profile.name =request.POST['name']
        user_profile.address =request.POST['address']
        user_profile.mobile =request.POST['mobile']
        user_profile.about =request.POST['about']
            
        try:
            user_profile.photo = request.FILES['photo']
            User_profile.save(self=user_profile)
        except:
            User_profile.save(self=user_profile)
        print("success")
        messages.info(request, 'Profile Updated Successfully')
        context = {
            'user_profile' :user_profile
        }
        return render(request,'adminapp/profile.html',context)
    else:
        userr = request.user
        user_profile = get_object_or_404(User_profile, user=userr)  
        context={
            'user_profile' : user_profile
        }
        return render(request,'adminapp/profile.html',context)
    # else:
    #     return HttpResponse("You are not Farmer")



@login_required(login_url='loginpage')
def Buyer_dashboard(request):
    user = request.user
    pur = Purchased.objects.filter(buyer = user)
    
    total_purchase_products = Purchased.objects.filter(buyer = user,accept = True)
    sum = 0
    for i in total_purchase_products:
        sum = sum+int(i.select_product.product_price)

    approved_order = Purchased.objects.filter(buyer = user,accept=True).count()


    context = {
        'pur' : pur,
        'approved_order' : approved_order,
        'total_purchase_products' : total_purchase_products,
        'sum':sum
    }
    return render(request,'adminapp/buyer-dashboard.html',context)




@login_required(login_url='loginpage')
def My_order(request):
    user = request.user
    pur = Purchased.objects.filter(buyer = user)
    context = {
        'pur' : pur
    }
    return render(request,'adminapp/my-order.html',context)



@login_required(login_url='loginpage')
def Buy_success(request,myid):
    user = request.user
    pro = ProductTbl.objects.get(id=myid)
    
    pur = Purchased(select_product = pro, buyer = user,seller=pro.upload_by)
    pur.save()
    messages.info(request,"Product Buy successfuly")
    return render(request,'farmerapp/buy_success.html')




@login_required(login_url='loginpage')
def Accept_order(request,myid):
    user = request.user
    if user.is_staff:
        pur = Purchased.objects.get(id = myid)
        pur.accept = True
        pro_id = pur.select_product.id
        pur.save()
        pro = ProductTbl.objects.get(id = pro_id)
        pro.sold = True
        pro.save()
        
        messages.info(request,"Order accepted")
        return redirect('orders')
    else:
        return HttpResponse("You are not former")



@login_required(login_url='loginpage')
def Reject_order(request,myid):
    user = request.user
    if user.is_staff:
        pur = Purchased.objects.get(id = myid)
        pur.reject = True
        print("REJECTED")
        pro_id = pur.select_product.id
        pur.save()
        pro = ProductTbl.objects.get(id = pro_id)
        pro.sold = False
        pro.save()
        
        messages.info(request,"Order Rejected")
        return redirect('orders')
    else:
        return HttpResponse("You are not former")











def Contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        cont = ContactTbl(name=name,email=email,subject=subject,message=message)
        cont.save()
        messages.info(request,"Contact sent successfully")
        return redirect('contact')
    else:
        return redirect('contact')




def available_product(request):
    cat = Product_catagory.objects.all()
    products = ProductTbl.objects.filter(sold = False)

    context = {
        'cat' : cat,
        'products' : products
    }
    return render(request,'farmerapp/available-product.html',context)




def sold_product(request):
    cat = Product_catagory.objects.all()
    products = ProductTbl.objects.filter(sold = True)

    context = {
        'cat' : cat,
        'products' : products
    }
    return render(request,'farmerapp/sold-product.html',context)




def search_item(request):
    if request.method == "GET":
        cat = Product_catagory.objects.all()
        search = request.GET['search']
        print(search)
        products = ProductTbl.objects.filter(product_name__icontains = search)
        context = {
        'cat' : cat,
        'products' : products
    }
    return render(request,'farmerapp/search_item.html',context)




def check_plant_disease(request):
    return render(request,'farmerapp/check_plant_disease.html')






import keras
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from PIL import Image
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np


def predict_disease(request):
    if request.method == "POST":
        leaf = request.FILES['leaf']
        sam = SampleImages(photo = leaf)
        sam.save()
        sa = SampleImages.objects.last()

        other_model = keras.models.load_model('ml_model/new_plant_disease_prediction.h5')
        test_image = load_img('media/'+ str(sa.photo),target_size=(150,150))
        test_image = img_to_array(test_image)/255
        test_image = np.expand_dims(test_image,axis=0)
        result = other_model.predict(test_image).round(3)
        pred = np.argmax(result)
        ans = ""
        if pred == 0:
            ans = "Diseased cotton plant"
        elif  pred == 1:
            ans = "diseased cotton plant"
        else:
            ans = "healthy cotton plant"



        return HttpResponse(f"PREDICTED RESULT IS : {ans}.")





