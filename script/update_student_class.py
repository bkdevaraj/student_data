import os
import sys
import django

# Get the current file directory
script_path = os.path.dirname(os.path.abspath(__file__))

# Get the project root directory
project_path = os.path.abspath(os.path.join(script_path, os.pardir))

# Add the project root directory to sys.path
sys.path.append(project_path)

# Set the DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_tennis_club.settings')

# Initialize Django
django.setup()

from datetime import datetime
from studentsdataform.models import Student

def update_student_class():
    # Get the current date and time
    now = datetime.now()

    # Check if it's March 21 at 12:18 PM
    if now.month == 6 and now.day == 12 and now.hour == 15 and now.minute == 50:
        
        # Update the student class
        students = Student.objects.all()
        for student in students:
            if student.student_class == '1':
                student.student_class = '2'
            elif student.student_class == '2':
                student.student_class = '3'
            elif student.student_class == '3':
                student.student_class = '4'
            elif student.student_class == '4':
                student.student_class = '5'
            elif student.student_class == '5':
                student.student_class = '6'
            elif student.student_class == '6':
                student.student_class = '7'
            elif student.student_class == '7':
                student.student_class = '8'
            elif student.student_class == '8':
                student.student_class = '9'
            elif student.student_class == '9':
                student.student_class = '10'
            elif student.student_class == '10':
                student.student_class = 'Please Enter as he passed 10th'
            elif student.student_class == 'lkg':
                student.student_class = 'ukg'
            elif student.student_class == 'ukg':
                student.student_class = '1'
            else:
                student.student_class = student.student_class + '+' + '1'
            # and so on for the other class updates
            student.save()

update_student_class()
