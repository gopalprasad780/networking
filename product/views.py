from django.shortcuts import render
from .models import Category
from django.views.generic.detail import DetailView
# Create your views here.

class CategoryDetailView(DetailView):
    model=Category
    template_name="product/categoryView.html"


