from django.shortcuts import render
from testapp.forms import StudentForm
def student_input_view(request):
    submitted = False
    name = ''
    if request.method == 'POST':
        form = StudentForm(request.POST) #overidding the empty form
        if form.is_valid():
            print("form validation is success and print data")
            print("Name:",form.cleaned_data['name'])
            print("Rollno:",form.cleaned_data['rollno'])
            print("Marks:",form.cleaned_data['marks'])
            submitted = True
            name = form.cleaned_data['name']
    form = StudentForm()  # empty form object to display form to end user
    return render(request,'testapp/std.html',{'form':form,'submitted':submitted, 'name':name})