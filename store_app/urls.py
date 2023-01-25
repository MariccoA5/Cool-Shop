from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search),
    path('cart/', views.cart, name='cart'),
    path('pet-store/', views.petstore),
    path('pet-store/<str:item>/', views.one_item),
    path('gun-store/', views.gunstore),
    path('gun-store/<str:item>/', views.one_item),
    path('grocery-store/', views.grocerystore),
    path('grocery-store/<str:item>/', views.one_item),
    path('add-product/<int:id>', views.add_product),
]   