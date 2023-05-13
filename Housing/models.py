from django.db import models

# Create your models here.


Accomchoices = models.TextChoices('Accomchoices','Hostel PayingGuest Flat')
class HousingModels(models.Model):
    location = models.TextField()
    Amenities = models.TextField()
    Rent = models.IntegerField()
    Deposit = models.IntegerField()
    AccomodationType = models.TextField(choices=Accomchoices.choices)
    profile = models.ImageField(upload_to="%(app_label)s_%(class)s_%(pk)s/")

class HouseImages():
    House = models.ForeignKey(HousingModels , on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="%(app_label)s_%(class)s_%(House)s/")
    class Meta:
        db_table = 'house images'
    
