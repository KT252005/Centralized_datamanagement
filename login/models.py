from django.db import models

# Create your models here.
class Chat_signup(models.Model):
   username=models.CharField(max_length=120,unique=True)
   first_name=models.CharField(max_length=120)
   last_name=models.CharField(max_length=120)
   email = models.EmailField(max_length=254, unique=True)
   password = models.CharField(max_length=128)
   date_joined = models.DateTimeField(auto_now_add=True)
   role=models.CharField(max_length=120,default="user")

   
   def __str__(self):
        return self.username



