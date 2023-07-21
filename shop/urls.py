from django.contrib import admin
from django.urls import path

from products.views import CancelView, SuccessView, CreateCheckoutSessionView, Products, ProductDetails

urlpatterns = [
    path('', Products.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetails.as_view(), name='product-details'),
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
