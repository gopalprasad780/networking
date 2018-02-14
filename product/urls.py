from django.urls import path
from django.views.generic import ListView
from .models import  Category

urlpatterns=[
        path('', ListView.as_view(model=Category, template_name='product/index.html', context_object_name='categories'), name='index'),
        ]

