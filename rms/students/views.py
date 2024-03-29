from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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
    qs_archieve = Archieve.objects.filter(archieve_id=qs.archieve_id)
    context = {
        'obj':qs,
        'results':qs_results,
        'archieve': qs_archieve
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
def update_achieve(request, typ,item_id,student_id,student_pk):
    template_name = 'students/update_achieve.html'
    qs = get_object_or_404(Archieve,pk=item_id)
    if request.method == 'POST':
        form = ArchieveForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archieve location successfully updated!')
            return redirect('students:student_details',pk=student_pk,student_id=student_id )
    else:
        context = {'form': ArchieveForm(instance=qs), 'obj': qs,'typ':typ,'student_id':student_id,}
    return render(request, template_name, context)


@login_required
def achieve_location(request):
    template_name = 'students/achieve_location.html'
    return render(request, template_name)

@login_required
def achieves(request):
    template_name = 'students/achieves.html'
    qs = Archieve.objects.all()
    return render(request, template_name,{'obj':qs})

def pdf_report_create(request,id):
    obj = get_object_or_404(Student,pk=id)
    template_path = 'students/student_pdf.html'
    context = {'obj': obj}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="students_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response