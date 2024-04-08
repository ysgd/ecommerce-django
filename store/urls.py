
from django.urls import path
from . import views
from views import CategoryViewSet, OrderViewSet, CustomerViewSet, ProductViewSet

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
]
