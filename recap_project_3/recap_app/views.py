from django.shortcuts import render
from recap_app.models import *

# Create your views here.
def student_list(request):
    student_data = StudentModel.objects.all()


    context = {
        'student_data': student_data
    }

    return render(request, 'student-list.html', context)



def student_create(request):
    
    return render(request, 'add-student.html')