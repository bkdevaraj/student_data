from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# Create your views here.
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from .templatetags import custom_filters
import datetime

from django.contrib import messages
# def studentdata(request):
#     if request.method == 'POST':
#         # Create a new student object with the form data
#         student = Student(
#             student_name=request.POST['student_name'],
#             father_name=request.POST['father_name'],
#             mother_name=request.POST['mother_name'],
#             student_class=request.POST['student_class'],
#             dob=request.POST['dob'],
#             aadhar=request.POST['aadhar'],
#             school_name=request.POST['school_name'],
#             student_aadhar=request.POST['student_aadhar'],
#             father_aadhar=request.POST['father_aadhar'],
#             mother_aadhar=request.POST['mother_aadhar'],
#             mobile_number=request.POST['mobile_number']
#         )

#         # Save the new student object to the database
#         student.save()

#         # Redirect the user to a success page
#         return redirect('success')
    
#     # Render the form template for GET requests
#     return render(request, 'student.html')


# HOME PAGE
def home(request):
    return render(request,'home.html')
# ADD STUDENT PAGE AND SAVING THE DATA TO MODEL
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('student_list')
            # return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# def studentdatabase(request):
#     students = Student.objects.all()
#     return render(request, 'studentdatabase.html', {'students': students})


# GENERATING STUDENTS LIST DATABASE AFTER SAVING TO MODEL






def student_list(request):
    students = Student.objects.all()

    # filter based on search query
    search_query = request.GET.get('search_box')
    if search_query:
        students = Student.objects.filter(
            Q(student_name__icontains=search_query) |
            Q(father_name__icontains=search_query) |
            Q(mother_name__icontains=search_query) |
            Q(student_class__icontains=search_query) |
            Q(school_name__icontains=search_query) |
            Q(student_aadhar__icontains=search_query) |
            Q(father_aadhar__icontains=search_query) |
            Q(mother_aadhar__icontains=search_query) |
            Q(mobile_number__icontains=search_query)
        )

        # try:
            
        #         search_date = datetime.datetime.strptime(search_query, '%Y-%m-%d').date()
        #         students = Student.objects.filter(dob=str(search_date))
        # except ValueError:
        #    print('data not suffi')

        # try:
        #     if search_query=='45':
        #         print('hi')
        #         age = int(search_query)
        #         today = datetime.date.today()
        #         birthdates = [today - relativedelta(years=age), today - relativedelta(years=age - 1)]
        #         students |= Student.objects.filter('dob__range= birthdates')
        # except ValueError:
        #     pass

    return render(request, 'studentdatabase.html', {'students': students, 'search_query': search_query})


def delete_students(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_ids')
        if student_ids:
            Student.objects.filter(id__in=student_ids).delete()
            
    return redirect('student_list')





def modify_student(request, student_id):
    # Get the student object by id, or return a 404 error if not found
    student = get_object_or_404(Student, id=student_id)

    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    # Render the modify_student.html template with the form and student data
    context = {'form': form, 'student': student}
    return render(request, 'modify_student.html', context)



def student_list_by_age(request):
    students = Student.objects.all()

    # filter based on age
    # students = students.filter(dob__lte=timezone.now() - relativedelta(years=18))

    # sort by age in descending order
    students = students.order_by('dob')

    return render(request, 'studentdatabase.html', {'students': students})
# for i in range(0,50):

#     VAL1=Student.objects.filter(id=i)
#     print(i,VAL1)


# import threading
# import time
# from datetime import datetime, timedelta
# from django.conf import settings
# from pytz import timezone
# import os
# import pytz


# # import threading
# # import time
# # from datetime import datetime, timedelta
# # from django.conf import settings
# # from .models import Student

# # # set the date and time for the class updates from a configuration file
# # CLASS_UPDATE_HOUR = int(settings.CLASS_UPDATE_HOUR)
# # CLASS_UPDATE_MINUTE = int(settings.CLASS_UPDATE_MINUTE)
# # CLASS_UPDATE_MONTH = int(settings.CLASS_UPDATE_MONTH)
# # CLASS_UPDATE_DAY = int(settings.CLASS_UPDATE_DAY)

# # def update_student_class():
# #     now = datetime.now()
# #     if now.month == CLASS_UPDATE_MONTH and now.day == CLASS_UPDATE_DAY and now.hour == CLASS_UPDATE_HOUR and now.minute == CLASS_UPDATE_MINUTE:
# #         students = Student.objects.all()
# #         for student in students:
# #             if student.student_class == '1':
# #                 student.student_class = '2'
# #             elif student.student_class == '2':
# #                 student.student_class = '3'
# #             elif student.student_class == '3':
# #                 student.student_class = '4'
# #             elif student.student_class == '4':
# #                 student.student_class = '5'
# #             elif student.student_class == '5':
# #                 student.student_class = '6'
# #             elif student.student_class == '6':
# #                 student.student_class = '7'
# #             elif student.student_class == '7':
# #                 student.student_class = '8'
# #             elif student.student_class == '8':
# #                 student.student_class = '9'
# #             elif student.student_class == '9':
# #                 student.student_class = '10'
# #             elif student.student_class == '10':
# #                 student.student_class = 'Please Enter as he passed 10th'
# #             elif student.student_class == 'lkg':
# #                 student.student_class = 'ukg'
# #             elif student.student_class == 'ukg':
# #                 student.student_class = '1'
# #             else:
# #                 student.student_class=student.student_class+'+'+'1'
# #             # and so on for the other class updates
# #             student.save()

# # def background_update():
# #     while True:
# #         update_student_class()
# #         time.sleep(60) # wait for one minute before running the function again

# # if settings.DEBUG:
# #     # run the function once at startup if in debug mode
# #     update_student_class()
# # else:
# #     # start a separate thread to run the function in the background if not in debug mode
# #     t = threading.Thread(target=background_update)
# #     t.daemon = True
# #     t.start()




