from django.db import models

class CategoryProduct(models.TextChoices):
    DRINK = "Drink"
    MEAT = "Meat"
    CANDY = "Candy"
    FRUIT = "Fruit"
    OTHER = "Other"

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(
        max_length=30,
        choices=CategoryProduct.choices,
        default=CategoryProduct.OTHER
    )
    price = models.DecimalField(decimal_places=2, max_digits=5)
