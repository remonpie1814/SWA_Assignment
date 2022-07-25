from contextlib import redirect_stderr
from tkinter import Button
from django.shortcuts import render,redirect
from .models import Coffee
from .forms import CoffeeForm
# Create your views here.
def index(request):
    return render(request,"index.html",{})



def coffee_view(request):
    # Coffee모델에 담긴 모든 객체를 coffee_all에 담는다
    coffee_all=Coffee.objects.all()
    # # 만약에 request가 POST면? #POST를 바탕으로 Form을 완성하고 Form이 유효하면 저장한다
    # if request.method=="POST":
    #     # POST의 내용을 바탕으로 form을 만든다
    #     form=CoffeeForm(request.POST)
    #     # 양식이 유효하면 .save()를 실행한다.
    #     if form.is_valid():
    #         form.save()
    

    form=CoffeeForm()
    
    return render(request,"coffee.html",{"coffee_list":coffee_all,"coffee_form":form})

def coffee_create(request):
    form=CoffeeForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("coffee_view")


def coffee_update(request,pk):
    coffee_all=Coffee.objects.all()
    
    form=CoffeeForm(request.POST)
    if coffee_all.get(id=pk).button_on==False:
        coffee_all.filter(id=pk).update(button_on=True)
        return redirect("coffee_view")
    if form.is_valid():
        coffee_all.filter(id=pk).update(name=str(form["name"].value()))
        coffee_all.filter(id=pk).update(price=int(form["price"].value()))
        coffee_all.filter(id=pk).update(is_ice=bool(form["is_ice"].value()))
        coffee_all.filter(id=pk).update(button_on=False)
    return redirect("coffee_view")

def coffee_delete(request,pk):
    record = Coffee.objects.get(id = pk)
    record.delete()
    return redirect("coffee_view")