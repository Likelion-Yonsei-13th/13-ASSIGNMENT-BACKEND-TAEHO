from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]
