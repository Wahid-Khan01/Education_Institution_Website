from django.db import models
# Create your models here.

from django.db import models



class IndianStates(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class IndiaCities(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile2(models.Model):


    COURSE_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Fullstack', 'Fullstack'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)



class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

