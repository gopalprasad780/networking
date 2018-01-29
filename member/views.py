from django.shortcuts import render
from django.http import HttpResponse
from .forms import  AddForm
from django.contrib.auth.models import User
from .models import Member, Profile
from product.models import Category, Product
from django.utils.transaction import gettext_lazy as _
# Create your views here.

def index(request):
    return render(request, 'member/index.html')


def add(request, member_id):
    if request.method == 'POST':
        form=AddForm(request.POST)
        if form.is_valid():
            sponser=form.cleaned_data['sponser']
            pin=form.cleaned_data['pin']
            group=form.cleaned_data['group']
            product=form.cleaned_data['product']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            mobile_number=form.cleaned_data['mobile_number']
            adhaar_number=form.cleaned_data['adhaar_number']
            bank_name=form.cleaned_data['bank_name']
            bank_account_no=form.cleaned_data['bank_account_no']
            ifsc_code=form.cleaned_data['ifsc_code']
            address=form.cleaned_data['address']
            district=form.cleaned_data['district']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pin']

            #validating sponser
            try:
                user=User.objects.get(username=sponser)
            except User.DoesnotExist:
                raise ValidationError(
                        _('Sponser : %(value)s is not valid'),
                        code='invalid',
                        params={'value':sponser},)
            return HttpResponse("The form is submitted successfully")
        else:
            return render(request, 'member/addform.html', {'form':form })

    else:
        form=AddForm()
        
        return render(request, 'member/addform.html', {'form':form }) 


def  detail(request, member_id):
    return HttpResponse('This is detail of submitted user')

