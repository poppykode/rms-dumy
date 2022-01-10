from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Department, LecturerDepartment
from .forms import DepartmentForm,LecturerDepartmentForm
from accounts.models import User

# Create your views here.

@login_required
def departments(request):
    template_name = 'department/departments.html'
    qs = Department.objects.all()
    context = {
        'obj':qs,
    }
    return render(request, template_name,context)
    
@login_required
def create_department(request):
    template_name = 'department/create_department.html'
    if request.method=='POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department successfully added.')
            return redirect('departments:departments')
    form = DepartmentForm()
    return render(request, template_name, {'form': form,'type':'create'})

@login_required
def add_department_to_lecturer(request, l_id):
    template_name = 'department/add_department_to_lecturer.html'
    qs = get_object_or_404(User,pk=l_id)
    print(qs.designation)
    if qs.designation == 'head of department':
        has_department = LecturerDepartment.objects.filter().exists()
        if has_department:
            messages.warning(request, 'HOD already has a department.')
            return redirect('accounts:user_details',pk=l_id )
    if request.method == 'POST':
        form = LecturerDepartmentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = qs
            new_form.save()
            messages.success(request, 'Department successfully added to Lecturer.')
            return redirect('accounts:user_details',pk=l_id )
    form = LecturerDepartmentForm()
    context ={
        'form':form,
        'obj':qs
    }
    return render(request,template_name,context)

@login_required
def remove_department_from_lecturer(request,d_id,l_id):
    qs = get_object_or_404(LecturerDepartment,pk=d_id)
    qs.delete()
    messages.success(request, 'Department successfully removed from Lecturer.')
    return  redirect('accounts:user_details',pk=l_id)


