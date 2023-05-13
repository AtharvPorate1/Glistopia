from django.db import models
from User import models as md
from aenum import NamedConstant
# Create your models here.


    

#model for storing mess data
class MessData(models.Model):
    
    messImage = models.ImageField(upload_to=f"uploads/Mess/messImage/",blank=True) #posts should be saved according to their post ids = "<location><public><postno>"
    menuImage = models.ImageField(upload_to=f"uploads/Mess/menuImage/", blank=True) #same comment as above
    messName = models.TextField()
    contactNo = models.IntegerField()
    profile = models.ImageField(upload_to="%(app_label)s_%(class)s_%(pk)s", blank=True)
    email = models.EmailField()
    location = models.TextField()
    #method for accepting value for subscription model

#mess images
class MessImages():
    mess = models.ForeignKey(MessData , on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to="%(app_label)s_%(class)s_%(mess)s")
    class Meta :
        db_table = 'mess images'
        

#mess subscription model
class Subscription(models.Model):
    messId = models.OneToOneField(MessData , on_delete=models.CASCADE)
    onceAday = models.IntegerField() #rates for one time food for day for month
    twiceAday = models.IntegerField() #rates for two time food for day for month
    
    
            


    
    


#model for rating and review of Mess food per user
class ratingAndReview(models.Model):
    MessId = models.ForeignKey(MessData , on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Reviews = models.TextField()
    UserId = models.OneToOneField('User.UserModel',on_delete=models.CASCADE)
    
