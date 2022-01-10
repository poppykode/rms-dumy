from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ArchieveForm
from .models import Student, StudentResult, Archieve


# Create your views here.
@login_required
def students(request):
    template_name = 'students/students.html'
    #get via endpoint
    qs = Student.objects.all()
    context = {
        'obj':qs,
    }
    return render(request, template_name,context)

@login_required
def student_details(request,pk,student_id):
    template_name = 'students/student_details.html'
    qs = get_object_or_404(Student,pk=pk)
    qs_results = StudentResult.objects.filter(student_id=student_id)
    context = {
        'obj':qs,
        'results':qs_results
    }
    return render(request, template_name,context)

@login_required
def archieve(request,typ,item_id,student_id):
    template_name = 'students/archieve.html'
    if typ=='student':
        qs = get_object_or_404(Student,pk=item_id)
    else:
        qs = get_object_or_404(StudentResult,pk=item_id)
    if request.method == 'POST':
        form = ArchieveForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.archieve_id = qs.archieve_id
            new_form.item_id = qs.student_id
            new_form.typ = typ
            new_form.save()
            qs.archieved = True
            qs.save()
            return redirect('students:student_details',pk=qs.pk,student_id=student_id )
    return render(request,template_name,{'form':ArchieveForm(),'typ':typ,'student_id':student_id,'obj':qs})

@login_required
def achieve_location(request):
    template_name = 'students/achieve_location.html'
    return render(request, template_name)

@login_required
def achieves(request):
    template_name = 'students/achieves.html'
    qs = Archieve.objects.all()
    return render(request, template_name,{'obj':qs})