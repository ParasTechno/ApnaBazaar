from django.contrib import admin

from mainApp.models import Brand, MainCategory, Product, SubCategory
from .models import *
admin.site.register((MainCategory,SubCategory,Brand,Product,Seller,Buyer,Wishlist,Checkout,Subscribe,Contact))
