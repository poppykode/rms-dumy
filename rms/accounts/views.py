from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from students.models import StudentResult
from .models import User
from students.models import Student

# Create your views here.
def login_view(request):
    template_name = 'registration/login.html'
    return render(request, template_name)

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if not user.is_active:
            messages.error(
                request, 'Your account has been deactivate, please contact Admin.')
            return redirect('accounts:login_view')
        auth.login(request, user)
        messages.success(request, 'You have successfully logged in.')
        return redirect('accounts:redirect_logged')
    else:
        messages.error(request, 'Invalid username or password.')
        return redirect('accounts:login_view')

@login_required
def admin_dashboard(request):
    template_name = 'accounts/dashboards/admin_dashboard.html'
    qs_student = Student.objects.all()
    qs_results = StudentResult.objects.all()
    total_students = qs_student.count()
    total_students_archieved = qs_student.filter(archieved = True).count()
    total_students_to_be_archieved = qs_student.filter(archieved = True).count()
    total_results =qs_results.count()
    context ={
        'total_students':total_students,
        'total_students_archieved' : total_students_archieved,
        'total_students_to_be_archieved':total_students_to_be_archieved,
        'total_results':total_results
    }
    return render(request,template_name,context)

@login_required
def redirect_logged(request):
    return redirect('accounts:admin_dashboard')   

@login_required
def users(request):
    template_name = 'accounts/users/users.html'
    usr =  request.user
    qs = User.objects.all().exclude(pk=usr.pk)
    context = {
        'obj':qs,
    }
    return render(request, template_name,context)

@login_required
def user_details(request,pk):
    template_name = 'accounts/users/user_details.html'
    qs = get_object_or_404(User,pk=request.user.pk)
    context = {
        'obj':qs
    }
    return render(request, template_name,context)

