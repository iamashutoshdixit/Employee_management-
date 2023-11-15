from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.


class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    



STATE_CHOICES=(
("Andhra Pradesh","Andhra Pradesh"),
("Arunachal Pradesh ","Arunachal Pradesh "),
("Assam","Assam"),
("Bihar","Bihar"),
("Chhattisgarh","Chhattisgarh"),
("Goa","Goa"),
("Gujarat","Gujarat"),
("Haryana","Haryana"),
("Himachal Pradesh","Himachal Pradesh"),
("Jammu and Kashmir ","Jammu and Kashmir "),
("Jharkhand","Jharkhand"),
("Karnataka","Karnataka"),
("Kerala","Kerala"),
("Madhya Pradesh","Madhya Pradesh"),
("Maharashtra","Maharashtra"),
("Manipur","Manipur"),
("Meghalaya","Meghalaya"),
("Mizoram","Mizoram"),
("Nagaland","Nagaland"),
("Odisha","Odisha"),
("Punjab","Punjab"),
("Rajasthan","Rajasthan"),
("Sikkim","Sikkim"),
("Tamil Nadu","Tamil Nadu"),
("Telangana","Telangana"),
("Tripura","Tripura"),
("Uttar Pradesh","Uttar Pradesh"),
("Uttarakhand","Uttarakhand"),
("West Bengal","West Bengal"),
("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
("Chandigarh","Chandigarh"),
("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
("Daman and Diu","Daman and Diu"),
("Lakshadweep","Lakshadweep"),
(" Delhi","Delhi"),
("Puducherry","Puducherry")
)


# Create your models here.

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField(null=True)
    state=models.CharField(choices=STATE_CHOICES,max_length=50)
    

    def __str__(self):
     return str(self.id)


Attendance_Choice =(
   ('Present','Present'),
   ('Absent','Absent'),
   ('Not Avilable','Not Avilable'),
   ('Ill','Ill'),
   ('None','None')
)
class Attendance(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   attendance=models.CharField(choices=Attendance_Choice,max_length=20)
   date_time=models.DateTimeField()

   def __str__(self):
     return str(self.id)



class Emp_Attendances(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   attendance=models.CharField(choices=Attendance_Choice,max_length=20)
   check_in=models.DateTimeField()
   #ckeckout=models.DateTimeField()

   def __str__(self):
     return str(self.id)
    
