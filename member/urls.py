"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
app_name='member'
urlpatterns = [
        path('', views.index, name='index'),
        path('tree/', views.tree, name='tree'),
        path('edit/<int:member_id>/', views.edit, name='edit'),
        path('addmember/', views.addmember, name="addmember"),
        path('add/<int:member_id>/', views.add, name='add'),
        path('login/', views.custom_login, name="login"),
        path('redirectlogin/', auth_views.login, {'template_name':'member/login.html'}, name='redirectlogin'),
        path('logout/', auth_views.logout, {'next_page':'/'}, name="logout"),


]

