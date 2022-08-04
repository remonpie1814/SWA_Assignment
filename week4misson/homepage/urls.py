from django.urls import path
from . import views

app_name="homepage"
urlpatterns = [
    path('', views.index, name='post_list'),
    path("whoami",views.whoami,name="whoami"),
    path("echo",views.echostr,name="echo"),
    path("weapon",views.weapon_view,name="weapon_view"),
    path("weapon/create",views.weapon_create,name="weapon_create"),
    path("weapon/update/<weapon_id>",views.weapon_update,name="weapon_update"),
    path("weapon/delete/<weapon_id>",views.weapon_delete,name="weapon_delete"),
]