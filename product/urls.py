from django.urls import path
from django.views.generic import ListView
from .models import  Category
from .views import CategoryDetailView
from django.views.generic.base import TemplateView
urlpatterns=[
        path('', ListView.as_view(model=Category, template_name='product/index.html', context_object_name='categories'), name='index'),
        path('<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
        path('about/', TemplateView.as_view(template_name='product/about.html'),name='about'),
        path('terms/', TemplateView.as_view(template_name='product/terms.html'),name="terms"),
        ]


