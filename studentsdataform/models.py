from django.db import models
from datetime import date
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator



import os
import uuid

def student_image_path(instance, filename):
    # Generate a unique identifier
    unique_id = uuid.uuid4().hex
    # Extract the file extension from the original filename
    file_extension = os.path.splitext(filename)[1]
    # Construct the unique filename
    unique_filename = f"{unique_id}{file_extension}"
    return os.path.join('assets/img/', unique_filename)


def validate_image_extension(value):
    if not value.name.endswith('.jpg') and not value.name.endswith('.jpeg') and not value.name.endswith('.png'):
        raise ValidationError("Only JPG, JPEG, and PNG images are allowed. and its better if 150 pixels in Horizontal and 200 pixels in Vertical")



def validate_image_size(value):
    # 150 KB
    max_size = 150 * 1024

    if value.size > max_size:
        raise ValidationError(f"The maximum file size allowed is {max_size/1024:.2f} KB.")

        
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
    age = models.IntegerField(null=True, blank=True,help_text="Do not Enter Age Field as its caluculated automatically")
    address=models.CharField(max_length=500, default='Unknown')
    remarks = models.CharField(max_length=500, blank=True, null=True, help_text="Add remarks about the student")
    image = models.ImageField(
         upload_to=student_image_path,
        blank=True,
        null=True,
        validators=[
            
            validate_image_extension,
            validate_image_size
           
        ]
    
    )
   
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
    