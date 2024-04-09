
from django.urls import path
from .views import CategoryViewSet, OrderViewSet, CustomerViewSet, ProductViewSet, UserViewSet, GroupViewSet

urlpatterns = [
  # path('home/', views.home, name='home'),
  path('Category', CategoryViewSet.as_view({'get':'list','post':'create'})),
  path('category/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('Order', OrderViewSet.as_view({'get':'list','post':'create'})),
  path('order/<int:pk>/',OrderViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('customer', CustomerViewSet.as_view({'get':'list','post':'create'})),
  path('customer/<int:pk>/',CustomerViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('product', ProductViewSet.as_view({'get':'list','post':'create'})),
  path('product/<int:pk>/',ProductViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('register/',UserViewSet.as_view({'post':'register'}),name='register'),
  path('login/',UserViewSet.as_view({'post':'login'}),name='login'),
  path('role/',GroupViewSet.as_view({'get':'list'}),name='role')
]
