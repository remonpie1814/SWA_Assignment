from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(default="name",max_length=20)
    price=models.IntegerField(default=0)
    is_ice=models.BooleanField(default=False)
    button_on=models.BooleanField(default=False)