from contextlib import redirect_stderr
from django.shortcuts import render,HttpResponse,redirect
from requests import request
import requests
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

@api_view(["GET"])
def weather_views(request):
    
    ipapiid=""
    apiid=""

    ipurl='http://api.ipstack.com/check?access_key=' + ipapiid
    res=requests.get(ipurl).json()
    lat=res["latitude"]
    lon=res["longitude"]
    
    url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,apiid)
    response=requests.get(url).json()

    # 온도를 K에서 섭씨로 변경
    temperature=float(response["main"]["temp"])-273.15
    # 도시명을 영문표기에서 한글표기로 바꿈. 사전에 없으면 그냥 영문표기 그대로.
    region_en_to_kr={"Seoul":"서울","Incheon":"인천","Daejeon":"대전","Daegu":"대구","Busan":"부산","Gwangju":"광주","Ulsan":"울산"}
    if res["city"] in region_en_to_kr:
        cityname=region_en_to_kr[res["city"]]
    else:
        cityname=res["city"]
    
    return render(request,"weather_view.html",{"current_temperature":round(temperature,1),"current_windspeed":response["wind"]["speed"],"current_region":cityname})

@api_view(["GET"])
def busstop_view(request):
    import pandas as pd
    import numpy as np
    df=pd.read_csv("homepage/data/bus.csv",encoding="cp949")

    ipapiid=""
    ipurl='http://api.ipstack.com/check?access_key=' + ipapiid
    res=requests.get(ipurl).json()
    lat=res["latitude"]
    lon=res["longitude"]

    # 정류장의 위도와 경도를 모두 n에 array형태로 담음
    n=np.array(df[["위도","경도"]])
    # 모든 정류장의 위도와 경도에서 현재 위치를 뺌
    n2=n-np.array([lat,lon])
    # 정류장위치-현재위치 한 벡터들의 norm을 계산해서 array로 만들음
    norm_n2=np.linalg.norm(n2,axis=1)

    # 그 중에서 가장 작은 norm의 index를 구해봄
    minindex=norm_n2.argmin()
    
    result=str(df.loc[minindex]["도시명"])+" "+str(df.loc[minindex]["정류장 명칭"])
    return render(request,"busstop.html",{"busstop":result})