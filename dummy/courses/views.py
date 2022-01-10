from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CourseForm,LecturerCourseForm
from .models import Course, LecturerCourse
from accounts.models import User

# Create your views here.
@login_required
def courses(request):
    template_name = 'courses/courses.html'
    qs = Course.objects.all()
    context = {
        'obj':qs,
    }
    return render(request, template_name,context)
    
@login_required
def create_course(request):
    template_name = 'courses/create_course.html'
    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course successfully added.')
            return redirect('courses:courses')
    form = CourseForm()
    return render(request, template_name, {'form': form,'type':'create'})

@login_required
def add_course_to_lecturer(request, l_id):
    template_name = 'courses/add_course_to_lecturer.html'
    qs = get_object_or_404(User,pk=l_id)
    if request.method == 'POST':
        form = LecturerCourseForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.lecturer = qs
            new_form.save()
            messages.success(request, 'Course successfully added to Lecturer.')
            return redirect('accounts:user_details',pk=l_id )
    form = LecturerCourseForm()
    context ={
        'form':form,
        'obj':qs
    }
    return render(request,template_name,context)

@login_required
def remove_course_from_lecturer(request,c_id,l_id):
    qs = get_object_or_404(LecturerCourse,pk=c_id)
    qs.delete()
    messages.success(request, 'Course successfully removed from Lecturer.')
    return  redirect('accounts:user_details',pk=l_id)

