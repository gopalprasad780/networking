from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

#Importing models from Product App
from product.models import Product
 

class Profile(models.Model):
     
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=13)
    adhaar=models.CharField(max_length=12, blank=True)
    bank_name=models.CharField(max_length=50)
    bank_account=models.CharField(max_length=20)
    bank_ifsc=models.CharField(max_length=11)
    address=models.CharField("Nearest Service Center" , max_length=100)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    image=models.ImageField(upload_to="user", default="user/none/no_img.png")

    def __str__(self):
        return self.user.username


    def get_fields(self):
        return "user, mobile, adhaar, bank_name, bank_account, bank_ifsc, address, district, state, pincode, image"



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# A Token class that will generate a pin for record
# It will have minimum value 1000 and have created date
# The main purpose is to track record for new pin generation
class Token(models.Model):
    created=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.pin

    def getpin(self):
        if self.id:
            return self.id + 10000
        else:
            return 0



# A Member Model is the main model which will be use by public
# Each entry in Member model will relates to transaction made by user
# It will records:
# 1. The sponser user
# 2. child user (new user) for which sponser is used
# 3. The product for which user is registered
# 4. The date and time the transaction is done
# 5.  Newly pin generated - The newly pin will be foreign key of model Token
# 
# It will contain method that checks:
# -- if user has completed its criteria of 16 member to win the prize
# -- if user has completed first row?
# -- if user's children has completed its first row, which will be 2nd row

    
class Member(models.Model):
    user=models.CharField(max_length=10)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    sponser=models.ForeignKey(User, on_delete=models.PROTECT)
    created=models.DateTimeField(auto_now=True)
    key_1=models.IntegerField(default=0, editable=False)
    key_2=models.IntegerField(default=0, editable=False)
    key_3=models.IntegerField(default=0, editable=False)
    key_4=models.IntegerField(default=0, editable=False)
    first_level=models.BooleanField(default=False, editable=False)
    second_level=models.BooleanField(default=False, editable=False)
    prize_win=models.BooleanField(default=False, editable=False)

    def get_fields(self):
        return "user, product, sponer, created, key_1,  key_2, key_3, key_4, first_level, second_level, prize_win"




    def save(self):
        if not self.id:
            keyone=Token.objects.create()
            self.key_1=keyone.getpin()

            keytwo = Token.objects.create()
            self.key_2=keytwo.getpin()

            keythree=Token.objects.create()
            self.key_3=keythree.getpin()

            keyfour=Token.objects.create()
            self.key_4=keyfour.getpin()

        super(Member, self).save()



    def __str__(self):
        return "User: %s  - Product: %s  - Sponser: %s -Key:[%s, %s, %s, %s]"%(self.user, self.product.name, self.sponser.username, self.key_1, self.key_2, self.key_3, self.key_4)

    def get_child(self):
            return [self.key_1, self.key_2, self.key_3, self.key_4]



        





