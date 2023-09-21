from django.urls import path
from .import views 

app_name = 'parentsdataform'
urlpatterns = [
    
    
    path('add_parent/', views.add_parent, name='add_parent'),
    path('parent_list/', views.parent_list, name='parent_list'),
    
    
   
    path('delete_parents/',views.delete_parents,name='delete_parents'),
     path('modify_parent/<int:parent_id>/', views.modify_parent, name='modify_parent'),
     path ('parent_list_by_age/', views.parent_list_by_age, name='parent_list_by_age'),
     
     path('parent_profile/<int:parent_id>/', views.parent_profile_view, name='parent_profile'),
     path('parent/<int:parent_id>/next/', views.next_parent_profile, name='next_parent_profile'),
    

]