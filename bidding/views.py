import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from farmerapp .models import ProductTbl, User_profile
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bid_sold, Bidded_price, BiddingProduct
import datetime



@login_required(login_url='loginpage')
def add_for_bidding(request):
    user = request.user
    user_pro = User_profile.objects.get(user = user)
    pro = ProductTbl.objects.filter(upload_by = user_pro)

    context = {
        'pro' : pro
    }
    return render(request,'bidding/add_for_bidding.html',context)



@login_required(login_url='loginpage')
def save_bid_data(request):
        if request.method == "POST":
            product_id = request.POST['select_product']
            bidding_date = request.POST['bidding_date']
            bidding_start_time = request.POST['bidding_start_time']
            bidding_end_time = request.POST['bidding_end_time']
            min_price = request.POST['min_price']

            product = ProductTbl.objects.get(id = product_id)
            try:
                bid_pro = BiddingProduct(product = product,bidding_date = bidding_date,bidding_start_time = bidding_start_time,bidding_end_time = bidding_end_time,min_price = min_price)
                bid_pro.save()
            except:
                messages.info(request,"This Product is already Biddedd")
                return redirect('add_for_bidding')
            messages.info(request,"Product addedd to Bidding Successfully")
            return redirect('add_for_bidding')

        else:
            messages.info(request,"Something went Wrong !!")
            return redirect('add_for_bidding')
   


@login_required(login_url='loginpage')
def view_upcoming_bids(request):
    user = request.user

    bid_pro = BiddingProduct.objects.filter(product__upload_by__user = user)
    today = datetime.date.today()
    
    context = {
        'bid_pro' : bid_pro,
        'today' : today
    }
    return render(request,'bidding/view_upcoming_bids.html',context)




def view_bid(request,myid):
    bid = BiddingProduct.objects.get(id = myid)
    bid_data = Bidded_price.objects.order_by('-bid_price').filter(bid_product = bid)


    context = {
        'bid': bid,
        'bid_data' : bid_data
    }
    return render(request,'bidding/view_bid.html',context)





def bidding_list(request):
    return render(request,'bidding/bidding_list.html')




def Sold_bid(request,myid):
    user = request.user
    data = Bidded_price.objects.get(id = myid)

    sol = Bid_sold(sold_by = user,bid_product = data)
    sol.save()
    bided_pro = BiddingProduct.objects.get(id = data.bid_product.id)
    bided_pro.complete = True
    bided_pro.save()

    return redirect('view_bid',bided_pro.id)




def Bid_pro(request):
    user = request.user
    bid_data = BiddingProduct.objects.filter(complete=False).order_by('bidding_date')
     
    context = {
        'bid_data': bid_data,
        'today' : datetime.date.today(),

    }
    return render(request,'bidding/bid_pro.html',context)




def Bid_pro_detail(request,myid):
    bid_prop = BiddingProduct.objects.get(id= myid)

    bid_data = Bidded_price.objects.order_by('-bid_price').filter(bid_product = bid_prop)[:10]
    context = {
        'bid_desc' : bid_prop,
        'today' : datetime.date.today(),
        'bid_data' : bid_data
    }
    return render(request,'bidding/bid_pro_detail.html',context)




def Place_bid(request,bid_pro_id):
    user = request.user
    bid_pro = BiddingProduct.objects.get(id = bid_pro_id)

    bid_price = request.POST['bid_price']

    bidded_pr = Bidded_price(bid_product = bid_pro,bid_price = bid_price,bidded_by = user)
    bidded_pr.save()
    messages.success(request,"Bid Placed")
    return redirect('bid_pro_detail',bid_pro_id)




def Complete_bid_list(request):
    user = request.user
    user_pro = User_profile.objects.get(user = user)
    sold = Bid_sold.objects.filter(sold_by = user)
    context = {
        'sold' : sold
    }
    return render(request,'bidding/complete_bid_list.html',context)




def buyer_biddings(request):
    user = request.user
    sold = Bid_sold.objects.filter(bid_product__bidded_by = user)
    context = {
        'sold' : sold
    }
    return render(request,'bidding/buyer_biddings.html',context)




import razorpay
import json
import numpy as np
import random

url = 'https://api.razorpay.com/v1'
client = razorpay.Client(auth=("rzp_live_w1RJIJNnHcqCdX", "bGeBWlvBemUuT64LKOGA5Rgn"))




@login_required(login_url='login')
def pay(request):
    # course = request.POST['course_name']
    # try:
        course_id = request.POST['course_name']
        user = request.user
        if request.method =='POST':

            customer_name = request.POST['customer_name']
            customer_email = request.POST['customer_email']
            customer_mobile= request.POST['customer_mobile']
            pay_amt = request.POST['pay_amt']
            course = request.POST['course_name']
            course_id = request.POST['course_id']
            pay_amt = float(pay_amt)
            print(type(pay_amt))
            pay_amt = pay_amt*100
            print(pay_amt)
            
            # cust = Customer(course= course, customer_name=customer_name,customer_email=customer_email,customer_mobile=customer_mobile,pay_amt=pay_amt)
            # cust.save()

            data = {
                'amount' : pay_amt,
                'currency' : "INR",
                'receipt': str(random.randint(100000,999999)),
                'notes':{
                    'name' : user.username,
                    'payment_for' : course + " " + "project",
                    'course_id' : course_id
                }
            }
            
            order = client.order.create(data=data)
            orderId = order["id"]
            oder_id = orderId
            print("Order id is",orderId)
            client.order.fetch(orderId)

            # cust = Customer.objects.last()
            # print(cust)
            context = {
                # 'cust' : cust,
                'orderId' : orderId,
                'customer_name' : customer_name,
                'customer_email' : customer_email,
                'customer_mobile' : customer_mobile,
                'pay_amt' : pay_amt,
                'course' : course,
                'course_id' : course_id
                

            }
            
            return render(request, 'bidding/pay.html',context)
        else:
            return redirect('product_detail',course_id)

    # except:
    #     return redirect('product_detail',course_id)







from django.views.decorators.csrf import csrf_exempt

from .models import Purchased_Project

@csrf_exempt
def success(request):
    try:
        user = request.user
        if request.method == 'POST':
            course_id = request.POST['course_id']
            course_name = request.POST['course_name']
            payment_id = request.POST['razorpay_payment_id']
            order_id = request.POST['razorpay_order_id']
            signature_hash = request.POST['razorpay_signature']
            course = request.POST['course_name']
            paid_amount = float(request.POST['paid_amount'])
          
            paid_amount = paid_amount/100

            sel_project = Bid_sold.objects.get(id = course_id)

            paid = Purchased_Project(user = user,sel_project = sel_project,payment_id = payment_id,signature_hash = signature_hash,project_name = course_name,paid_amount = paid_amount)
            paid.save()
            #client.payment.capture(payment_id, amount)
            
            data = client.payment.fetch(payment_id)
            context = {
                'payment_id' : payment_id,
                'course' : course,
                'paid_amount' : paid_amount,
                

            }
            return render(request,'paymentapp/pay_success.html',context)
        else:
            return HttpResponse('<script>window.history.back();</script>')   
        
    except:
        return HttpResponse('<script>window.history.back();</script>')    





