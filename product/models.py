from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    amount=models.DecimalField("Participation Amount", decimal_places=2, max_digits=10)
    image=models.ImageField(upload_to="category", default="category/none/no_img.png")

    def get_fields(self):
        return "name, description, amount, image"




    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="product", default="product/none/no_img.png")

    def __str__(self):
        return self.name

    def get_fields(self):
        return "category, name, image"


