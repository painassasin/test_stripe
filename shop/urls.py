from django.contrib import admin
from django.urls import path

from products.views import CancelView, CreateCheckoutSessionView, Products, SuccessView

urlpatterns = [
    path('', Products.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]
