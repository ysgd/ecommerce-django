
from django.urls import path
from .views import CategoryViewSet, OrderViewSet, CustomerViewSet, ProductViewSet, UserViewSet, GroupViewSet, home, product, search, likeView

urlpatterns = [
  path('home/', home, name='home'),
  path('product/<int:pk>/', product, name='product'),
  path('search/', search, name='search'),
  path('Category/', CategoryViewSet.as_view({'get':'list','post':'create'})),
  path('category/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('Order/', OrderViewSet.as_view({'get':'list','post':'create'})),
  path('order/<int:pk>/',OrderViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('customer/', CustomerViewSet.as_view({'get':'list','post':'create'})),
  path('customer/<int:pk>/',CustomerViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('product/', ProductViewSet.as_view({'get':'list','post':'create'})),
  path('product/<int:pk>/',ProductViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  path('register/',UserViewSet.as_view({'post':'register'}),name='register'),
  path('login/',UserViewSet.as_view({'post':'login'}),name='login'),
  path('role/',GroupViewSet.as_view({'get':'list'}),name='role'),
  path('like/<int:pk>/', likeView, name='like_product')
]
