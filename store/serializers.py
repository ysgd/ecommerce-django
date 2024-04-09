from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import Category, Customer, Product, Order, User

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id','name']
    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password', 'groups']
    
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('name',)
    
class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['firstName','lastName','email']
    
class ProductSerializers(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ['productName', 'category', 'price']
    
class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'