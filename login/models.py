from django.db import models

# Create your models here.
class signup_data(models.Model):
   username=models.CharField(max_length=120,unique=True)
   first_name=models.CharField(max_length=120)
   last_name=models.CharField(max_length=120)
   email = models.EmailField(max_length=254, unique=True)
   password = models.CharField(max_length=128)
   date_joined = models.DateTimeField(auto_now_add=True)
   role=models.CharField(max_length=120,default="user")

   
   def __str__(self):
        return self.username


class Organizations_data(models.Model):
   Gst_no= models.CharField(max_length=16,unique=True)
   Company_name=models.CharField(max_length=50)
   Domain=models.CharField(max_length=100)
   Address=models.CharField(max_length=100)
   city=models.CharField(max_length=50)
   State = models.CharField(max_length=50)
   Pincode = models.CharField(max_length=6, unique=True)
   contact_info = models.CharField(max_length=10, unique=True)
   created_at = models.DateTimeField(auto_now_add=True)  
   updated_at=models.DateTimeField(auto_now_add=True)
 
   def __str__(self):
       return self.Company_name
   