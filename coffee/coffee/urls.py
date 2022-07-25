"""coffee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from homepage.views import index,coffee_view,coffee_create,coffee_update,coffee_delete

urlpatterns = [
    path("",index),
    path("coffee/",coffee_view,name="coffee_view"),
    path("createcoffee/",coffee_create,name="coffee_create"),
    path("coffee/<pk>/",coffee_update,name="coffee_update"),
    path("coffeedelete/<pk>/",coffee_delete,name="coffee_delete"),
    path('admin/', admin.site.urls),
]
