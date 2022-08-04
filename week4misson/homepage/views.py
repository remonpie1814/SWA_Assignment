from contextlib import redirect_stderr
from django.shortcuts import render,HttpResponse,redirect
from requests import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Weapon
from .forms import WeaponForm

def index(requests):
    return render(requests,"index.html",{})
# Create your views here.

@api_view(["GET"])
def whoami(requests):
    return JsonResponse({"name":"yeji1814"})

@api_view(["GET"])
def echostr(requests):
    str=requests.GET.get("string",None)
    return JsonResponse({"value":str})

@api_view(["GET"])
def weapon_view(requests):
    weapon_all=Weapon.objects.all()
    return render(requests,"weapon_view.html",{"weapon_list":weapon_all})

@api_view(["POST"])
def weapon_create(requests):
    create_weapon=WeaponForm(requests.POST)
    if create_weapon.is_valid():
        create_weapon.save()
    create_weapon=WeaponForm()
    return redirect("/weapon/")

@api_view(["POST"])
def weapon_update(requests,weapon_id):
    weapon_all=Weapon.objects.all()
    form=WeaponForm(requests.POST)
    if form.is_valid():
        weapon_all.filter(id=weapon_id).update(name=str(form["name"].value()),stock=int(form["stock"].value()))
    return redirect("/weapon/")

@api_view(["POST"])
def weapon_delete(request,weapon_id):
    record = Weapon.objects.get(id = weapon_id)
    record.delete()
    return redirect("/weapon/")