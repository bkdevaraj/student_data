from django.urls import path
from .import views 

app_name = 'studentsdataform'
urlpatterns = [
    
    path('home', views.home, name='home'),
    # path('',views.studentdata,name='studentdata'),
    path('add-student/', views.add_student, name='add_student'),
    # path('studentdatabase/', views.studentdatabase, name='studentdatabase'),
    path('student_list/',views.student_list,name='student_list'),
    path('delete_students/',views.delete_students,name='delete_students'),
     path('modify_student/<int:student_id>/', views.modify_student, name='modify_student'),
     path ('student_list_by_age/', views.student_list_by_age, name='student_list_by_age'),
     path('logout/', views.logout_view, name='logout'),
     path('student_profile/<int:student_id>/', views.student_profile_view, name='student_profile'),
     path('student/<int:student_id>/next/', views.next_student_profile, name='next_student_profile'),

]
    #  path('update_class/', views.update_class_view, name='update_class'),
    
      
    #  path('list/', views.StudentListView.as_view(), name='student_list'),
    
