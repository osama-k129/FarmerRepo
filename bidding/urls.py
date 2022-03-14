from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    # path('',views., name=''),
    path('add_for_bidding',views.add_for_bidding, name='add_for_bidding'),
    path('save_bid_data',views.save_bid_data, name='save_bid_data'),
    path('view_upcoming_bids',views.view_upcoming_bids, name='view_upcoming_bids'),
    path('view_bid/<int:myid>/',views.view_bid, name='view_bid'),

    path('bidding_list',views.bidding_list, name='bidding_list'),
    path('sold_bid/<int:myid>/',views.Sold_bid,name="sold_bid"),
    path('bid_pro',views.Bid_pro,name="bid_pro"),
    path('bid_pro_detail/<int:myid>/',views.Bid_pro_detail,name="bid_pro_detail"),
    path('place_bid/<int:bid_pro_id>/',views.Place_bid,name="place_bid"),

    path('complete_bid_list',views.Complete_bid_list, name='complete_bid_list'),

    path('buyer_biddings',views.buyer_biddings,name="buyer_biddings"),


    path('pay',views.pay,name='pay'),
    path('success',views.success,name='success'),



]