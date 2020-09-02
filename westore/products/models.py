from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="category_products", on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand, related_name="brand_products", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name