from django.shortcuts import render
from recap_app.models import *

# Create your views here.
def student_list(request):
    return render(request, 'student-list.html')