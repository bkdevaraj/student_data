
from django.shortcuts import render,redirect,get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from .models import Parent
from .forms import ParentForm
from django.db.models import Q
# Create your views here.
def add_parent(request):
    if request.method == 'POST':
        try:
            image = request.FILES['image']
        except MultiValueDictKeyError:
            image = None

        form = ParentForm(request.POST, request.FILES)
        
        if form.is_valid():
            parent = form.save(commit=False)
            
            if image is not None:
                parent.image = image
            
            parent.save() 
            return redirect('parentsdataform:parent_list')
    else:
        form = ParentForm()
        
    return render(request, 'parentsdataform/parents_form.html', {'form': form})


def parent_list(request):
    parents = Parent.objects.all()

    # filter based on search query
    search_query = request.GET.get('search_box')
    if search_query:
        parents = Parent.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(middle_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(occupation__icontains=search_query) |
            Q(pan_number__icontains=search_query) |
            Q(aadhar_number__icontains=search_query) |
            Q(mobile_number__icontains=search_query)
        )

        # try:
            
        #         search_date = datetime.datetime.strptime(search_query, '%Y-%m-%d').date()
        #         parents = parent.objects.filter(dob=str(search_date))
        # except ValueError:
        #    print('data not suffi')

        # try:
        #     if search_query=='45':
        #         print('hi')
        #         age = int(search_query)
        #         today = datetime.date.today()
        #         birthdates = [today - relativedelta(years=age), today - relativedelta(years=age - 1)]
        #         parents |= parent.objects.filter('dob__range= birthdates')
        # except ValueError:
        #     pass

    return render(request, 'parentsdataform/parentsdatabase.html', {'parents': parents, 'search_query': search_query})





from django.core.files.storage import default_storage
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=Parent)
def delete_parent_image(sender, instance, **kwargs):
    if instance.image and not instance.image.name.endswith('no_image.png'):
        if default_storage.exists(instance.image.name):
            default_storage.delete(instance.image.name)

def delete_parents(request):
    if request.method == 'POST':
        parent_ids = request.POST.getlist('parent_ids')
        if parent_ids:
            for parent_id in parent_ids:
                parent = Parent.objects.get(id=parent_id)
                delete_parent_image(sender=Parent, instance=parent)
                parent.delete()
            
    return redirect('parentsdataform:parent_list')





from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest

def modify_parent(request, parent_id):
    # Get the parent object by id, or return a 404 error if not found
    parent = get_object_or_404(Parent, id=parent_id)

    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES, instance=parent)
        if form.is_valid():
            if 'image' in request.FILES:
                new_image = request.FILES['image']
                if new_image.size > 150 * 1024:
                     form.add_error('image', "Image size should be less than 150KB.")
                allowed_types = ['image/jpeg', 'image/jpg', 'image/png']
                if new_image.content_type not in allowed_types:
                     form.add_error('image', "Invalid image type. Only jpg, jpeg, and png are allowed.")
                if parent.image:
                    # Delete the old image using default_storage
                    default_storage.delete(parent.image.name)
                # Save the new image using default_storage
                parent.image.save(new_image.name, new_image)

            parent = form.save()  # Save the form with or without the image

            return redirect('parentsdataform:parent_list')
        
    else:
        form = ParentForm(instance=parent)

    # Render the modify_parent.html template with the form and parent data
    context = {'form': form, 'parent': parent}
    return render(request, 'parentsdataform/modify_parent.html', context)



def parent_list_by_age(request):
    parents = Parent.objects.all()

    # filter based on age
    # parents = parents.filter(dob__lte=timezone.now() - relativedelta(years=18))

    # sort by age in descending order
    parents = parents.order_by('dob')

    return render(request, 'parentsdataform/parentsdatabase.html', {'parents': parents})
# for i in range(0,50):

#     VAL1=parent.objects.filter(id=i)
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
# # from .models import parent

# # # set the date and time for the class updates from a configuration file
# # CLASS_UPDATE_HOUR = int(settings.CLASS_UPDATE_HOUR)
# # CLASS_UPDATE_MINUTE = int(settings.CLASS_UPDATE_MINUTE)
# # CLASS_UPDATE_MONTH = int(settings.CLASS_UPDATE_MONTH)
# # CLASS_UPDATE_DAY = int(settings.CLASS_UPDATE_DAY)

# # def update_parent_class():
# #     now = datetime.now()
# #     if now.month == CLASS_UPDATE_MONTH and now.day == CLASS_UPDATE_DAY and now.hour == CLASS_UPDATE_HOUR and now.minute == CLASS_UPDATE_MINUTE:
# #         parents = parent.objects.all()
# #         for parent in parents:
# #             if parent.parent_class == '1':
# #                 parent.parent_class = '2'
# #             elif parent.parent_class == '2':
# #                 parent.parent_class = '3'
# #             elif parent.parent_class == '3':
# #                 parent.parent_class = '4'
# #             elif parent.parent_class == '4':
# #                 parent.parent_class = '5'
# #             elif parent.parent_class == '5':
# #                 parent.parent_class = '6'
# #             elif parent.parent_class == '6':
# #                 parent.parent_class = '7'
# #             elif parent.parent_class == '7':
# #                 parent.parent_class = '8'
# #             elif parent.parent_class == '8':
# #                 parent.parent_class = '9'
# #             elif parent.parent_class == '9':
# #                 parent.parent_class = '10'
# #             elif parent.parent_class == '10':
# #                 parent.parent_class = 'Please Enter as he passed 10th'
# #             elif parent.parent_class == 'lkg':
# #                 parent.parent_class = 'ukg'
# #             elif parent.parent_class == 'ukg':
# #                 parent.parent_class = '1'
# #             else:
# #                 parent.parent_class=parent.parent_class+'+'+'1'
# #             # and so on for the other class updates
# #             parent.save()

# # def background_update():
# #     while True:
# #         update_parent_class()
# #         time.sleep(60) # wait for one minute before running the function again

# # if settings.DEBUG:
# #     # run the function once at startup if in debug mode
# #     update_parent_class()
# # else:
# #     # start a separate thread to run the function in the background if not in debug mode
# #     t = threading.Thread(target=background_update)
# #     t.daemon = True
# #     t.start()

from django.shortcuts import render, get_object_or_404
from .models import Parent  # You might need to adjust this import based on your project structure

def parent_profile_view(request, parent_id):
    parent = get_object_or_404(Parent, id=parent_id)
    prev_parent = Parent.objects.filter(id__lt=parent_id).last()  # Get the previous parent
    next_parent = Parent.objects.filter(id__gt=parent_id).first()  # Get the next parent
    return render(request, 'parentsdataform/parent_profile.html', {'parent': parent,'prev_parent': prev_parent, 'next_parent': next_parent})

from django.http import HttpResponse
def next_parent_profile(request, parent_id):
    next_parent = Parent.objects.filter(id__gt=parent_id).order_by('id').first()
    if next_parent:
        return render(request, 'parentsdataform/parent_profile.html', {'parent': next_parent})
    else:
        # Handle case where there is no next parent
        return HttpResponse("No next parent available")
