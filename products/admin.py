from django.contrib import admin

from products.models import Product, StripeCheckoutSession


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_price')


@admin.register(StripeCheckoutSession)
class StripeCheckoutSessionAdmin(admin.ModelAdmin):
    list_display = ('uid', 'product', 'status')
    list_filter = ('status',)
    readonly_fields = ('stripe_id', 'status', 'customer_email')
    fieldsets = (
        (None, {'fields': ('product', 'customer_email')}),
        ('Stripe', {'fields': ('stripe_id', 'status')}),
    )
