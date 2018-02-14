from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from .forms import  AddForm
from django.contrib.auth.models import User
from .models import Member, Profile
from product.models import Category, Product
from django.utils.translation import gettext_lazy as _
# Create your views here.
from django import forms
def index(request):
    user=User.objects.get(username=10001)
    return render(request, 'member/index.html', {'user':user})

def addmember(request):
    member=Member.objects.get(user=10002)
    return render(request, 'member/addmember.html', {'member':member})


# member/add/<parent_id>/?key=key

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
            pincode=form.cleaned_data['pincode']

            #Creating user
            if User.objects.filter(username=pin).exists() is False:
                user=User.objects.create(username=pin, email=email, first_name=first_name, last_name=last_name)
            else:
                raise forms.ValidationError(_("Pin already user"), code="invalid")


            #editing user profile
            user.profile.mobile=mobile_number
            user.profile.adhaar=adhaar_number
            user.profile.bank_name=bank_name
            user.profile.bank_account=bank_account_no
            user.profile.bank_ifsc=ifsc_code
            user.profile.address=address
            user.profile.district=district
            user.profile.state=state
            user.profile.pincode=pincode
            user.save()

            member=Member()
            member.user=pin
            member.sponser=sponser
            member.product=product
            member.save()
            return redirect(reverse('member:index'))
        else:
            return render(request, 'member/addform.html', {'form':form }) 

    else:
        try:
            member=Member.objects.get(user=member_id)
        except Member.DoesNotExist:
            raise Http404("The Member id {} doesnot exist, Please check!!".format(member_id))
        product=member.product
        group=product.category
        key=request.GET.get('key',None)
        data={
                'sponser':member.user,
                'group':group.id,
                'pin':key,
                }

        form=AddForm(initial=data)
        #filtering product based on group
        form.base_fields['product'].queryset=product.category.product_set.all()
        #making fields readonly
        if key in ['', None]:
            for field in ['group','sponser']:
                form.base_fields[field].widget.attrs['readonly']=True
        else:
            for field in ['group','pin','sponser']:
                form.base_fields[field].widget.attrs['readonly']=True




        
        return render(request, 'member/addform.html', {'form':form }) 


def edit(request, member_id):
    member = get_object_or_404(User, pk=member_id)
    return render(request, 'member/editform.html', {'member':'member'})



def tree(request, member_id):
    try:
        member=Member.objects.get(user=member_id)
    except Member.DoesNotExist:
        raise Http404("Member doesnot Exist")
    tree=member_tree(member_id)

    return render(request, 'member/tree_view.html', {'tree':tree, 'member':member})
        
  


#definition to check all the child node
def member_tree(member_id=0):
    tree={}
    if Member.objects.filter(user=member_id).exists():
        member=Member.objects.get(user=member_id)
        for child in member.get_child():
            if Member.objects.filter(user=child).exists():
                tree[child]=Member.objects.get(user=child).get_child()
            else:
                tree[child]=[0,0,0,0]
        return tree
    else:
        tree[member_id]=[0,0,0,0]
        return tree


