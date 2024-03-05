from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    image_url = models.ImageField()

    def __str__(self) -> str:
        return self.name

class CartItem(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    product_id = models.OneToOneField(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()