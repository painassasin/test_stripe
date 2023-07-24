import uuid

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)  # cents

    @property
    def display_price(self) -> str:
        return '${0:.2f}'.format(self.price / 100)

    @property
    def stripe_price_data(self) -> dict:
        return {
            'currency': 'usd',
            'unit_amount': self.price,
            'product_data': {
                'name': self.name,
            },
        }

    def __str__(self):
        return self.name


class StripeCheckoutSession(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stripe_id = models.CharField(max_length=255, unique=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    customer_email = models.EmailField(null=True, blank=True)
