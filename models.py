from django.db import models

# Create your models here.

class AddEmployee(models.Model):
    fullname = models.CharField(max_length=100)
    empid=models.IntegerField()
    designation=models.CharField(max_length=100)
    date=models.DateField()
    department=models.CharField(max_length=100)
    annualctc=models.IntegerField()
    experience=models.IntegerField() 

class AddLatestNews(models.Model):
    details=models.TextField(max_length=1000)
    
class CalenderEvent(models.Model):
    date=models.DateField()
    occasion=models.TextField()
    
class AddJobOpening(models.Model):
    job=models.CharField(max_length=100)
    experience=models.IntegerField()
    skill=models.CharField(max_length=100)
    currentctc=models.IntegerField()
    noticeperiod=models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)