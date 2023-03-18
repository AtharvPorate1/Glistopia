from django.db import models

# Create your models here.


class housing(models.Model):
    house_image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    rent = models.IntegerField()

    def __str__(self):
        return self.name[0:50]
    
    
