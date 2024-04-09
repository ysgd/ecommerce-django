from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Category, Customer, Order, Product, User
from .serializers import CategorySerializer,CustomerSerializer,ProductSerializers,GroupSerializer,OrderSerializer, UserSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAdminUser
from django.db.models import Q, Count
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
  products = Product.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
  return render(request, 'home.html', {'products':products})

def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})

def likeView(request, pk):
  product = get_object_or_404(Product, id=request.POST.get('product_id'))
  product.likes.add(request.user)
  return HttpResponseRedirect(reverse('product', args=[str(pk)]))
 
def search(request):
	# Determine if they filled out the form
	if request.method == "POST":
		searched = request.POST['searched']
		# Query The Products DB Model
		searched = Product.objects.filter(Q(productName__icontains=searched) | Q(description__icontains=searched))
		# Test for null
		if not searched:
			messages.success(request, "That Product Does Not Exist...Please try Again.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})


class GroupViewSet(ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [AllowAny]
  
class CustomerViewSet(ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  permission_classes = [AllowAny]
  
class CategoryViewSet(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminUser]
  
class ProductViewSet(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  permission_classes = [AllowAny]
    
  
class OrderViewSet(ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [AllowAny]
  
class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
  
  def register(self,request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      password = request.data.get('password')
      hash_password = make_password(password)
      a = serializer.save()
      a.password = hash_password
      a.save()
      return Response("user created")
    else:
      return Response(serializer.errors)
    
  def login(self,request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username=email,password=password)
    
    if user == None:
      return Response('invalid credentials!')
    else:
      token,_ = Token.objects.get_or_create(user=user)
      return Response(token.key)