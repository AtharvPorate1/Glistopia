from django.db import models

# Create your models here.

#model for storing mess data
class MessData(models.Model):
    messImage = models.ImageField(upload_to=f"uploads/Mess/messImage/") #posts should be saved according to their post ids = "<location><public><postno>"
    menuImage = models.ImageField(upload_to=f"uploads/Mess/menuImage/") #same comment as above
    messName = models.TimeField()
    contactNo = models.IntegerField(max_length=10)
    
    onceAday = models.IntegerField() #rates for one time food for day for month
    twiceAday = models.IntegerField() #rates for two time food for day for month

    def charges(self):
        return [self.onceAday , self.twiceAday]

    #choices for subscription field
    class subtype(models.IntegerChoices):
        onceAday : int
        twiceAday : int
        def __init__(self ):
            self.onceAday = MessData.charges[0]
            self.twiceAday =MessData.charges[1]
            


    subscription = models.IntegerField(choices=subtype.choices)
    location = models.TextField()
    


#model for rating and review of Mess food per user
class ratingAndReview(models.Model):
    MessId = models.ForeignKey(MessData , on_delete=models.CASCADE)
    Rating = models.IntegerField(max=10)
    Reviews = models.TextField()
    