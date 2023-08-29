from django.db import models
from datetime import date
from django.utils import timezone
from datetime import timedelta

class Student(models.Model):
    student_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    student_class = models.CharField(max_length=150)
    school_name = models.CharField(max_length=150)
    student_aadhar = models.CharField(max_length=150)
    father_aadhar = models.CharField(max_length=150)
    mother_aadhar = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=150)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=500, default='Unknown')
    image = models.ImageField(upload_to='assets/img/', blank=True, null=True)
   
    # def save(self, *args, **kwargs):
        
    #     today = date.today()
    #     if self.dob:
    #         age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    #         self.age = age
        
    def __str__(self):
        return self.student_name
    

    # def age(self):
    #     today = date.today()
    #     age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    #     return age
    # def age(self):
    #     if self.dob:
    #         today = date.today()
    #         age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    #         return age
    #     else:
    #         return None
    