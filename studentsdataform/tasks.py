# from background_task import background
# from studentsdataform.models import Student
# from django.utils import timezone
# @background(schedule="cron 0 31 3 * *")
# def update_student_class():
#     students = Student.objects.all()
#     for student in students:
#         if student.student_class == '1':
#             student.student_class = '2'
#         elif student.student_class == '2':
#             student.student_class = '3'
#         elif student.student_class == '3':
#             student.student_class = '4'
#         elif student.student_class == '4':
#             student.student_class = '5'
#         elif student.student_class == '5':
#             student.student_class = '6'
#         elif student.student_class == '6':
#             student.student_class = '7'
#         elif student.student_class == '7':
#             student.student_class = '8'
#         elif student.student_class == '8':
#             student.student_class = '9'
#         elif student.student_class == '9':
#             student.student_class = '10'
#         elif student.student_class == '10':
#             student.student_class = 'Please Enter as he passed 10th'
#         elif student.student_class == 'lkg':
#             student.student_class = 'ukg'
#         elif student.student_class == 'ukg':
#             student.student_class = '1'
#         else:
#             student_class = student.student_class.split('+')
#             new_class = int(student_class[0]) + 1
#             student.student_class = f"{new_class}{'+'.join(student_class[1:])}"
#         student.save()
