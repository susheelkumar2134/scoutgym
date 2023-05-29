from django.db import models

# Create your models here.
class User_Details(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=20)
    class Meta:
        db_table = 'UserForm' #This line for register name in databases Ex:- 'UserForm'.
        
    