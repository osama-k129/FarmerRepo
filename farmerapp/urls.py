from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    # path('',views., name=''),
    path('',views.Index, name='index'),
    path('index',views.Index, name='index'),
    path('base',views.Base, name='base'),
    path('loginpage',views.Loginpage, name='loginpage'),
    path('sign-in',views.Sign_in, name='sign-in'),
    path('logout',views.Logout, name='logout'),


    path('about',views.About, name='about'),
    path('contact',views.Contact, name='contact'),
    path('our-product',views.Our_product, name='our-product'),


    path('profile',views.Profile, name='profile'),
    path('admin-base',views.Admin_base, name='admin-base'),
    path('dashboard',views.Dashboard, name='dashboard'),
    path('add-product',views.Add_product, name='add-product'),
    path('product-list',views.Product_list, name='product-list'),
    path('sales-report',views.Sales_report, name='sales-report'),
    path('orders',views.Orders, name='orders'),



    path('edit_profile',views.Edit_profile, name='edit_profile'),
    path('delete_product/<int:myid>/',views.Delete_product, name='delete_product'),
    path('edit_product/<int:myid>/',views.Edit_product, name='edit_product'),
    path('catagory/<int:myid>/',views.Catagory, name='catagory'),
    path('product-detail/<int:myid>/',views.Product_detail, name='product_detail'),


    path('buyer-dashboard',views.Buyer_dashboard, name='buyer-dashboard'),
    path('buy-success/<int:myid>/',views.Buy_success, name='buy-success'),
    path('my-order',views.My_order, name='my-order'),
    path('accept-order/<int:myid>/',views.Accept_order, name='accept-order'),
    path('contact_us',views.Contact_us, name='contact_us'),


    path('available_product',views.available_product, name='available_product'),
    path('sold_product',views.sold_product, name='sold_product'),
    path('reject-order/<int:myid>/',views.Reject_order, name='reject-order'),
    path('search_item',views.search_item, name='search_item'),

    path('check_plant_disease',views.check_plant_disease, name='check_plant_disease'),
    path('predict_disease',views.predict_disease, name='predict_disease'),



]