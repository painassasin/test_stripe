from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)  # cents

    @property
    def display_price(self) -> str:
        return '${0:.2f}'.format(self.price / 100)

    def __str__(self):
        return self.name
