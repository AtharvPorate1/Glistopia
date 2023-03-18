from django.db import models

# Create your models here.


class Food(models.Model):
    food_image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    subscription = models.TextField(max_length=100) 

    def __str__(self):
        return self.name[0:50]