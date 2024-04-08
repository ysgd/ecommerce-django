from django.db import models
from django.contrib.auth.models import AbstractUser 
import datetime

# Create your models here.

class User(AbstractUser):
  email = models.EmailField(unique=True)
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
class Category(models.Model):
  categoryName = models.CharField(max_length=90)
  description = models.TextField()
  
  def __str__(self):
    return self.categoryName
  
class Customer(models.Model):
  firstName = models.CharField(max_length=200)
  lastName = models.CharField(max_length=200)
  phone = models.CharField(max_length=10)
  email = models.EmailField(max_length=254)
  password = models.CharField(max_length=50)
  
  def __str__(self):
    return self.firstName
  
class Product(models.Model):
  productName = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/products/')
  
  def __str__(self):
    return self.productName
  
class Order(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  address = models.CharField(max_length=100)
  phone = models.CharField(max_length=10, blank=True)
  date = models.DateField(default=datetime.datetime.today)
  status = models.BooleanField(default=False)
  
  