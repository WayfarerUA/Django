"""hw1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path

from hw1app.views import firsturl, secondurl, nexturl, afternexturl, first_dynamic_url, third_dynamic_url, \
    fourth_dynamic_url, fifth_dynamic_url, regex, phone

urlpatterns = [
    path('', firsturl),
    path('articles/', secondurl),
    path('articles/archive/', nexturl),
    path('users/', afternexturl),
    path('article/<int:article_number>/', first_dynamic_url),
    path('article/<int:article_number>/archive/', third_dynamic_url),
    path('article/<int:article_number>/<slug:slug_text>/', fourth_dynamic_url),
    path('users/<int:users_number>/', fifth_dynamic_url),
    re_path(r'^(?P<regular>([1-9a-f-])({,4})', regex),
    #re_path(r'^(?P<reg>[1-9a-f-].{6})', phone),

]