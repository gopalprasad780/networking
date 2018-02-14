from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=250)
    amount=models.DecimalField("Participation Amount", decimal_places=2, max_digits=10)
    max_range=models.DecimalField("Max amount", decimal_places=2, default=0,  max_digits=10)
    min_range=models.DecimalField("Min amount", decimal_places=2, default=0,  max_digits=10)

    image=models.ImageField(upload_to="category", default="category/none/no_img.png")

    def product_range(self):
        return "{} - {} ".format(self.min_range, self.max_range)

    def get_fields(self):
        return "name, description, amount, image, min_range, max_range"




    def __str__(self):
        return "{} {} ".format( self.name, self.amount)


class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product", default="product/none/no_img.png")

    def __str__(self):
        return self.name

    def get_fields(self):
        return "category, name, image"


