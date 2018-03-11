from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=250)
    amount=models.DecimalField("Co-operation Amount", decimal_places=2, max_digits=10)
    max_range=models.DecimalField("Max Gift Amount", decimal_places=2, default=0,  max_digits=10)
    min_range=models.DecimalField("Min Gift Amount", decimal_places=2, default=0,  max_digits=10)
    seller=models.DecimalField("Seller Share", decimal_places=2, default=0, max_digits=10)
    sponser=models.DecimalField("Sponser Share", decimal_places=2, default=0, max_digits=10)
    consolation=models.DecimalField("Consolation ", decimal_places=2, default=0, max_digits=10)

    

    image=models.ImageField(upload_to="category", default="category/none/no_img.png")

    def product_range(self):
        return "{} - {} ".format(self.min_range, self.max_range)

    def get_fields(self):
        return "name, description, amount, image, min_range, max_range, seller, sponser, consolation"




    def __str__(self):
        return "{} {} ".format( self.name, self.amount)


SC_CHOICES=(
        ('LP','LAPTOP'),
        ('MB','MOBILE'),
        ('TV','LED TV'),
        ('FR','FRIDGE'),
        ('WM','WASHING MACHINE'),
        ('WP','WATER PURIFIER'),
        ('KU','KITCHEN UTENSIL'),
        )


class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category=models.CharField(max_length=2,choices=SC_CHOICES, default='MB')    
    code=models.CharField('Product Code',max_length=8, default='00000000')
    comment=models.CharField(max_length=300, blank=True, null=True)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product", default="product/none/no_img.png")
    is_active=models.BooleanField(default=True)
    created=models.DateField(auto_now=True, auto_now_add=False)



    def __str__(self):
        return self.name

    def get_fields(self):
        return "category, name, image, sub_category, comment, is_active, created"
    def gen_code(self):
        # code to get convert 'Name Group' to 'NG'
        g=''.join([i[0].upper() for i in self.category.name.split()])
        sg=self.sub_category
        pk=str(self.pk)

        return g+sg+str.zfill(pk,4)




