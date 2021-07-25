from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)



urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/',views.registerUser,name="register"),
    path('',views.getRoutes,name="routes"),
    path('users/',views.getUsers,name="users"),
    path('users/profile/',views.getUserProfile,name="user-profile"),
    path('products/',views.getProducts,name="products"),
    path('products/<str:pk>/',views.getProduct,name="product"),
]