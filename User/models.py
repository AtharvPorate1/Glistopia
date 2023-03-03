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
    lastLogin = models.DateTimeField("login date time ") #every time the user logins date and time should be overwritten in the date and time section
    

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

#model for storing service provider data
class ServiceProvider(models.Model):
    UserId = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    serviceProvided = models.TextField()
    serviceId = models.ForeignKey(Services , on_delete=models.CASCADE)


def user_directory_path(instance ):
    return 'user_{}'.format(instance.UserModel.UserId)

#moddel for storing Accomodation provider data
class AccomodationProvider(models.Model):
    UserId = models.ForeignKey(UserModel , on_delete=models.CASCADE)
    location = models.TextField()
    images = models.ImageField(upload_to=f'uploads/Accomodation/{user_directory_path}')
    size = models.IntegerField("Size of in square feet")
    noOfRooms = models.TextField() #this will contain input like 1BHK , 1RK etc.
    Rent = models.IntegerField()
    deposit = models.IntegerField()
    postedOn = models.DateField(auto_now_add=True)

#model for storing mess service owner data
class MessProvider():
    userId = models.ForeignKey(UserModel , on_delete=models.CASCADE)
    location = models.TextField()
    isTiffinAvailable = models.BooleanField()
    onceADay = models.IntegerField() #mess rates for one time mess facility in a day for a month 
    twiceADay = models.IntegerField() #mess rates for twice a day for a month
    orderRate = models.IntegerField() #normal order rates for food


    
