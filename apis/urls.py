from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.categoryList, name='categories'),
    path('category/detail/<str:pk>/', views.categoryDetail, name='category details'),
    path('category/create/', views.categoryCreate, name='category-create'),
    path('category/update/<str:pk>', views.categoryUpdate, name='category-create'),
    path('category/delete/<str:pk>', views.categoryDelete, name= 'category-delete'),
    path('product/', views.productList, name='product-list'),
    path('product/<str:pk>', views.productList, name='products'),
    path('product/create/', views.productCreate, name='product-create'),
    path('product/update/<str:pk>', views.productUpdate, name='product-update'),
    path('product/delete/<str:pk>', views.productDelete, name='product-delete'),
]