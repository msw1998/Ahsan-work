from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)  # Product name (Text)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price (Decimal)
    description = models.TextField()  # Product description (Large text)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return self.name  # This makes the name appear in the admin panel
