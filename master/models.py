from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Institution(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TrainingCourses(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    fee = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TrainingLead(models.Model):
    name = models.CharField(max_length=100)
    institution = models.ForeignKey(Institution,on_delete=models.PROTECT)
    course = models.ForeignKey(Course,models.PROTECT)
    year_of_passout = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=15)
    enquery_date = models.DateField()
    enquery_for = models.ForeignKey(TrainingCourses,null=True,on_delete=models.PROTECT,related_name='enq_course')
    remarks = models.TextField(null=True)
    followup = models.DateField(null=True)
    lastfollowup = models.DateField(null=True)
    status = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



