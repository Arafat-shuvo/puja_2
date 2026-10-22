from django.urls import path
from recap_app.views import *



urlpatterns = [
    path('', student_list, name='student_list'),
    path('add-student/', student_create, name='student_create'),
]