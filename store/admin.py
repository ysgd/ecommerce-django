from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, Customer, User, Order
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
