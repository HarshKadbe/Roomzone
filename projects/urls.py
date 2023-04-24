from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name="index"),
    path('login/', views.LoginPage, name="login"),
    path('register/', views.RegisterPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('listProperty/', views.ListPropertyFormView, name="list-property"),
    path('productdescription/<str:pk>/', views.ProductDescription, name="product-description"),
    path('products/filter/<int:category_id>/', views.FilterPage, name="filter-page"),
    path('userprofile/', views.UserProfile, name="user-profile"),
    path('userproperty/', views.UserProperty, name="user-property"),
    
    
    
]
