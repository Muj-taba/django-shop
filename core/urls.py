
from django.urls import path
from .views import ProductList ,  ProductDetail ,add_to_cart

app_name = 'core'

urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),

]

