from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    item1={"id":1,"name":"연필","price":1000,"url":"item01.html"}
    item2={"id":2,"name":"지우개","price":500,"url":"item02.html"}
    item3={"id":3,"name":"리코더","price":6000,"url":"item03.html"}
    item4={"id":4,"name":"트라이앵글","price":5000,"url":"item04.html"}
    item5={"id":5,"name":"스케치북","price":3000,"url":"item05.html"}
    item6={"id":6,"name":"공책","price":1000,"url":"item06.html"}
    item7={"id":7,"name":"돋보기","price":1500,"url":"item07.html"}
    item8={"id":8,"name":"실내화","price":3000,"url":"item08.html"}

    item_arr=[item1,item2,item3,item4,item5,item6,item7,item8]
    return render(request,"index.html",{"item_arr":item_arr})


def cart(request):
    return render(request,"cart.html")

def item(request,itemurlid):
    return render(request,"item0{}.html".format(itemurlid))

def about(request):
    return render(request,"about.html")