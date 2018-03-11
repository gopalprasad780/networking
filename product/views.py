from django.shortcuts import render
from .models import Category, SC_CHOICES,Product
from django.views.generic.detail import DetailView
from django.views import View
# Create your views here.

class CategoryDetailView(DetailView):
    model=Category
    template_name="product/categoryView.html"

class IndexView(View):
    template_name="product/index.html"
    categories=Category.objects.all()
    # filtering latest product based on sub category choices
    products=[]
    for sh in SC_CHOICES:
        product=Product.objects.filter(sub_category=sh[0]).last()
        #check if the result is not None
        if not product is None:
            products.append(product)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'products':self.products, 'categories':self.categories})


