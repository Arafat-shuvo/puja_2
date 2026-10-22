from django.shortcuts import redirect, render

from recap_app.forms import StudentForm
from recap_app.models import StudentModel

# Create your views here.
def student_list(request):
    student_data = StudentModel.objects.all()


    context = {
        'student_data': student_data
    }

    return render(request, 'student-list.html', context)



def student_create(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'add-student.html', {'form': form})