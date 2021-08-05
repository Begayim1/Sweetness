# from django.contrib import admin
from django.urls import path

from . import  views   #точка это текуший файл
from  .class_views import  *

urlpatterns = [

    path('', CategoryListView.as_view(), name='home'),
    path('list/', ShopListView.as_view(), name='list'),
    path('favorites/', ShopFavoritesView.as_view(), name='favorites'),
    path('product/<int:id>/', ShopDetailView.as_view(), name='detail'),
    path('product/create/', ShopCreateView.as_view(), name='create-product'),
    path('product/update/<int:id>/', ShopUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:id>/', ShopDeleteView.as_view(), name='delete_product'),
    path('search', SearchListView.as_view(), name='search'),


    #cart urls

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]
