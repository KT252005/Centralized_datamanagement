from django.db import models

# Create your models here.
class signup_data(models.Model):
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=120, default="user")

    def __str__(self):
        return self.username


class Allocation(models.Model):
    user = models.ForeignKey("signup_data", verbose_name=(""), on_delete=models.CASCADE)
    Startup_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Use auto_now=True to track last modification time
     
    def __str__(self):
        return self.user.username

class funding(models.Model):
    user= models.ForeignKey("signup_data", verbose_name=("User"), on_delete=models.CASCADE)
    Startup_name = models.CharField(max_length=50)
    Amount=models.CharField(max_length=20)
    Amount_used = models.CharField(max_length=20)
    Date=models.DateField( auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    