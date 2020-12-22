"""learn_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',views.first, name="first"),
    path('first_api/',views.firstApi, name="first_api"),
    path('sum', views.addNos, name='sum'),
    path('file_api/',views.fileApi, name="file"),
    path('check_password/',views.checkPassword, name="check_password"),
    path('check_user/',views.checkUsername, name="check_user"),
    path('save_user/',views.saveUsername, name="save_user"),
    path('view_products/',views.viewProducts, name="view_products"),
    path('view_all_products/',views.viewAllProducts, name="view_all_products"),
    path('sum_of_numbers/',views.sum_of_numbers, name="sum_of_numbers"),
    path('sum_of_numbers_log/',views.sum_of_numbers_with_log, name="sum_of_numbers_log"),
]
