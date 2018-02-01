from django import forms
from django.utils.translation import gettext_lazy as _
#This contains form for different models

from .models import Profile, Member 
from product.models import Category, Product
from django.contrib.auth.models import User
# fields from User profile
# title, mobile, adhaar, bank_name, bank_account, bank_ifsc, address,
# district, state, pincode
class ProfileAddForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('mobile','adhaar','bank_name','bank_account','bank_ifsc', 'address','district','state','pincode')
        labels ={
                 
                'mobile':_('Mobile Number'),
                'adhaar':_('Adhaar Number'),
                'bank_name':_('Bank Name'),
                'bank_account':_('Account Number'),
                'bank_ifsc':_('IFSC Code'),
                'address':_('Corresponding Address'),
                'district':_('District'),
                'state':_('state'),
                'pincode':_('PIN Code')
                }

        help_texts={
                'mobile':_('Please enter your 10 digit phone number'),
                'adhaar':_('Please enter your 12 digit Adhaar number'),
                'bank_name':_('Please enter a valid bank name'),
                'pincode':_('Pin Code must be of 6 digits'),
                }

        

#fields from User (django user model)
#first_name, last_name, email, username
class UserAddForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields=['first_name','last_name','email','username']




#field to be taken from member profile
#product, sponser
class MemberAddForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=['product','sponser']
        
        

class AddForm(forms.Form):
    sponser=forms.CharField(max_length=30)
    pin=forms.CharField(max_length=30)
    group=forms.ModelChoiceField(queryset=Category.objects.all())
    product=forms.ModelChoiceField(queryset=Product.objects.all())
    
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    mobile_number=forms.CharField(max_length=30)
    adhaar_number=forms.CharField(max_length=30)
    bank_name=forms.CharField(max_length=30)
    bank_account_no=forms.CharField(max_length=30)
    ifsc_code=forms.CharField(max_length=15)
    address=forms.CharField(widget=forms.Textarea)
    district=forms.CharField(max_length=15)
    state=forms.CharField(max_length=30)
    pincode=forms.CharField(max_length=6)

    def clean_sponser(self):
        super().clean()
        data=self.cleaned_data['sponser']
        try:
            user=User.objects.get(username=data)

        except User.DoesNotExist:
            raise forms.ValidationError(_('The sponser doesnot exist'),code='invalid-user')

        return user


    def clean_product(self):
        super().clean()
        group=self.cleaned_data['group']
        product = self.cleaned_data['product']

        if product not in group.product_set.all():

            raise forms.ValidationError(_('The product is not valid choice'), code='invalid')

        return product


    def clean_pin(self):
        sponser_data=self.clean_sponser()
        try:
            sponser=Member.objects.get(user=sponser_data.username)
        except Member.DoesNotExist:
            raise forms.ValidationError(_("The sponser & its pin doesnot match"), code="invalid")


        key_1=sponser.key_1
        key_2=sponser.key_2
        key_3=sponser.key_3
        key_4=sponser.key_4

        try:
            data=int(self.cleaned_data['pin'])
        except ValueError:
            raise forms.ValidationError(_('Pin should be numeric only'),code="invalid")

        
        print(key_1, key_2, key_3, key_4,'pin is', data)
        try:
            user=User.Objects.get(username=data)
            raise forms.ValidationError(_("Pin already used""Try another one"), code="invalid")
        except:
            pass

        if not data in [key_1, key_2, key_3, key_4]:
            raise forms.ValidationError(_("Incorrect Pin"" please ask your sponser"),code="invalid")
        return data




    



    
    
