from django.urls import path
from . import api_views

urlpatterns = [
    path('students/',api_views.student_list),
    path('students/add/', api_views.add_student),
    path('students/<int:id>/', api_views.student_detail),
    path('students/update/<int:id>/', api_views.update_student),
    path('students/delete/<int:id>/', api_views.delete_student),
]