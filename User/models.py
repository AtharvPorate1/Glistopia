from django.db import models

# Create your models here.

#model for user
class UserModel(models.Model):
    
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    mobile = models.IntegerField(max_length=10)
    UserId = models.AutoField(primary_key=True)
    IsStudent = models.BooleanField()
    IsServiceProvider = models.BooleanField()

    class Meta:
        db_table = "user"




 

#Student model 
class Student(models.Model):
    StudentId = models.ForeignKey(UserModel)
    college = models.TextField()
    location = models.TextField() #location college
    SearchingFor = models.TextField() #service searching for
    date = models.DateTimeField(auto_now=True)


#model for sevices and their service ids
class Services(models.Model):
    services = models.TextField()
    serviceId = models.AutoField(primary_key=True)


#models for Accomodation 
class AccomodationSeeker(models.Model):
    nearCollege = models.BooleanField()
    locationToSearch = models.TextField()
    '''if nearCollege == True :
        locationToSearch = Student.location''' # add this line as a condition to determine the nearest location to search 
    
    UserId = models.OneToOneField(UserModel , on_delete=models.CASCADE)

    class Meta :
        db_table = "accomodation"
    

class MessSeeker(models.Model):
    UserId = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    nearCollege = models.BooleanField()
    locationToSearch = models.TextField() 
    '''if nearCollege == True :
        locationToSearch = Student.location''' # add this line as a condition to determine the nearest location to search 
    
    class Meta :
        db_table = "mess Seeker"
    
