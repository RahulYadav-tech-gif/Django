from django.db import models 
 
# Create your models here. 
 
class Student(models.Model): 
    name = models.CharField(max_length=100) 
    age = models.IntegerField() 
    email = models.TextField() 
    address = models.ImageField(null = True, blank = True) 
 
 
class Car(models.Model):
    car_name = models.TextField()
    speed = models.IntegerField()

    def __str__(self) -> str:
        return self.car_name 