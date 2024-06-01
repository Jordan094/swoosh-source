from django.urls import path
from . import views
from .views import Favourites

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_to_favourites/', views.add_to_favourites, name='add_to_favourites'),
    path('remove_from_favourites/', views.remove_from_favourites, name='remove_from_favourites'),
    path('favourites/', Favourites, name='favourites'),
]
