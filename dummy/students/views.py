import requests
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import Course

from dummy.utils import generate_student_number,cal_final_mark
from django.conf import settings

URL = settings.BASE_URL


from .models import Student, StudentResult
from .forms import StudentForm, StudentResultForm,StudentCourseWorkForm

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
def create_student(request):
    template_name = 'students/create_student.html'
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            qs_course = get_object_or_404(Course,pk =request.POST.get('course'))
            new_student = Student.objects.create(
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                national_id_number = request.POST.get('national_id_number'),
                dob = request.POST.get('dob'),
                phone_number = request.POST.get('phone_number'),
                religion = request.POST.get('religion'),
                next_of_kin = request.POST.get('next_of_kin'),
                relationship = request.POST.get('relationship'),
                next_of_kin_phone_number = request.POST.get('next_of_kin_phone_number'),
                address = request.POST.get('address'),
                course =qs_course,
                student_id_number = generate_student_number()
            )
            if new_student:
                payload={
                    "student_id":new_student.pk,
                    "course":new_student.course.name,
                    "student_id_number":new_student.student_id_number,
                    "national_id_number":new_student.national_id_number,
                    "first_name":new_student.first_name,
                    "last_name":new_student.last_name,
                    "dob":new_student.dob,
                    "phone_number":new_student.phone_number,
                    "religion":new_student.religion,
                    "next_of_kin":new_student.next_of_kin,
                    "relationship":new_student.relationship,
                    "next_of_kin_phone_number":new_student.next_of_kin_phone_number,
                    "address":new_student.address
                }
                r=requests.post(URL+'/api/v1/students/create/student',payload)
                print(r.status_code)
            messages.success(request, 'Student successfully added.')
            return redirect('students:students')
    form = StudentForm()
    return render(request, template_name, {'form': form,'type':'create'})

@login_required
def add_results_to_student(request, s_id):
    template_name = 'students/add_results_to_student.html'
    qs = get_object_or_404(Student,pk=s_id)
    if request.method == 'POST':
        form = StudentResultForm(request.POST)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.student = qs
            # new_form.save()
            new_results = StudentResult.objects.create (
                student = qs,
                code = request.POST.get('code'), 
                module_name = request.POST.get('module_name'),
                mark =request.POST.get('mark'),
                grade = request.POST.get('grade'), 
                gpe =request.POST.get('gpe'), 
                credits = request.POST.get('credits'),
            )
            if new_results:
                payload ={
                    "student_id":new_results.student.pk,
                    "student_result_id":new_results.pk,
                    "student":new_results.student.first_name +' '+new_results.student.last_name,
                    "code":new_results.code,
                    "module_name":new_results.module_name,
                    "mark":new_results.mark,
                    "grade":new_results.grade,
                    "gpe":new_results.gpe,
                    "credits":new_results.credits
                }
                r=requests.post(URL+'/api/v1/students/create/student_result',payload)
                print(r.status_code)
            messages.success(request, 'Results successfully added to Student.')
            return redirect('students:student_details',pk=s_id )
    form = StudentResultForm()
    context ={
        'form':form,
        'obj':qs
    }
    return render(request,template_name,context)

@login_required
def student_details(request,pk):
    template_name = 'students/student_details.html'
    qs = get_object_or_404(Student,pk=pk)
    context = {
        'obj':qs,
    }
    return render(request, template_name,context)

@login_required
def add_course_work_marks_to_student(request, s_id):
    template_name = 'students/add_course_work_marks_to_student.html'
    qs = get_object_or_404(Student,pk=s_id)
    if request.method == 'POST':
        form = StudentCourseWorkForm(request.POST)
        if form.is_valid():
            quizz_mark = request.POST.get('quizz_mark')
            quizz_total = request.POST.get('quizz_total')
            group_mark = request.POST.get('group_mark')
            group_total = request.POST.get('group_total')
            presentation_mark = request.POST.get('presentation_mark')
            presentation_total = request.POST.get('presentation_total')
            test_mark = request.POST.get('test_mark')
            test_total = request.POST.get('test_total')
            new_form = form.save(commit=False)
            new_form.student = qs
            new_form.final_mark = cal_final_mark(quizz_mark,quizz_total,group_mark,group_total,presentation_mark,presentation_total,test_mark,test_total)
            new_form.save()
            messages.success(request, 'Course work successfully added to Student.')
            return redirect('students:student_details',pk=s_id )
    form = StudentCourseWorkForm()
    context ={
        'form':form,
        'obj':qs
    }
    return render(request,template_name,context)