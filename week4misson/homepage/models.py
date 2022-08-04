from django.db import models

# Create your models here.
class Weapon(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(default="",max_length=20)
    stock=models.IntegerField(default=0)
