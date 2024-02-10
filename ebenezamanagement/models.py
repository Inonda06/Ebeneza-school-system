from django.db import models
from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser




LEVELS=[
    ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')
]

TOPICS={
    ('Maths','Maths'),
    ('Science','Science'),
    ('Kiswahili','Kiswahili'),
    ('English','English'),
    ('History','History')
}


class User(AbstractUser):
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Parent(models.Model):
    Name= models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Name.first_name} {self.Name.last_name}'




class Student(models.Model):
    Name=models.OneToOneField(User, on_delete=models.CASCADE)
    Grade=models.CharField(max_length=150, choices=LEVELS)
    admNo=models.IntegerField()
    Guardian=models.ForeignKey(Parent,on_delete=models.CASCADE)
    Lunch=models.FloatField(default=0)
    Transport=models.FloatField(default=0)
    Fee=models.FloatField(default=0)
    FeeBalance=models.FloatField(default=15000)
    DateJoined=models.DateTimeField(auto_now=True)
    DateLeft=models.DateTimeField(auto_now=True)
    performance=models.ForeignKey('Subjects',on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return f'{self.Name.first_name} {self.Name.last_name}'

    



class teacher(models.Model):
    Name=models.OneToOneField(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=150,choices=TOPICS)
    classteacher=models.BooleanField()
    NationalID=models.IntegerField()

    def __str__(self):
        return f'{self.Name.first_name} {self.Name.last_name}'




class Subjects(models.Model):
    Name=models.CharField(max_length=120)
    Grade=models.CharField(max_length=120, choices=LEVELS)

    def __str__(self):
        return self.Name

class Department(models.Model):
    Name=models.CharField(max_length=120)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    Head=models.CharField(max_length=120)

    def __str__(self):
        return self.Name


class Examination(models.Model):
    Namme=models.ForeignKey(Student,on_delete=models.CASCADE)
