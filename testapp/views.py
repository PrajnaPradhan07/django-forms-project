from django.shortcuts import render
from testapp.forms import StudentForm
def student_input_view(request):
    form = StudentForm()
    return render(request,'testapp/std.html',{'form':form})