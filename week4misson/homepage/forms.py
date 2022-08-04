
from django import forms
from .models import Weapon

class WeaponForm(forms.ModelForm):
    class Meta:
        model=Weapon
        fields=("name","stock")