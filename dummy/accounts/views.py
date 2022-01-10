from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .models import User
from department.models import LecturerDepartment
from students.models import Student
from .forms import AddUserSignUpForm
from dummy.utils import send_password_and_username, generate_password



# Create your views here.
def login_view(request):
    # if request.user:
    #     return redirect('accounts:redirect_logged')
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
def redirect_logged(request):
    user = request.user
    if user.is_admin:
        return redirect('accounts:admin_dashboard')   
    else:
        return redirect('accounts:user_details',pk=request.user.pk)
        
@login_required
def hod_dashboard(request):
    template_name = 'accounts/dashboards/hod_dashboard.html'
    return render(request, template_name)

@login_required
def admin_dashboard(request):
    template_name = 'accounts/dashboards/admin_dashboard.html'
    qs_users = User.objects.all()
    total_system_users = qs_users.count()
    total_system_lectures = qs_users.filter(designation='lecturer').count()
    total_system_hods = qs_users.filter(designation='head of department').count()
    qs_students = Student.objects.all().count()
    context = {
        'total_system_users':total_system_users,
        'total_system_lectures':total_system_lectures,
        'total_system_hods':total_system_hods,
        'total_students':qs_students

    }
    return render(request, template_name,context)

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
    qs = get_object_or_404(User,pk=pk)
    print(qs.designation)
    if qs.designation == 'head of department':
        print('we are here')
        qs_department_id = LecturerDepartment.objects.filter(user=pk).exists()
        if qs_department_id:
            department_id = get_object_or_404(LecturerDepartment,user=pk)
            qs_department_lecturers = LecturerDepartment.objects.filter(department=department_id.department.pk).exclude(user=pk)
            context = {
                'obj':qs,
                'lecturers':qs_department_lecturers
            }
            return render(request, template_name,context)
    context = {
        'obj':qs,
    }
    return render(request, template_name,context)


@login_required
def toggle_user_status(request, pk):
    qs = get_object_or_404(User, pk=pk)
    if qs.is_active == True:
        qs.is_active = False
        qs.save()
        messages.warning(request, 'Status successfully deacivated.')
        return redirect('accounts:users')
    else:
        qs.is_active = True
        qs.save()
        messages.success(request, 'Status successfully activated.')
        return redirect('accounts:users')

@login_required
def user_signup(request):
    template_name = 'registration/user_signup.html'
    if request.method == 'POST':
        designation = request.POST.get('designation')
        email =request.POST.get('email')
        username = request.POST.get('username')
        is_lecturer = False
        is_admin = False
        is_hod = False
        if designation == 'admin':
            is_admin = True
        elif  designation == 'admin':
            is_lecturer = True
        else:
            is_hod = True
        user = User.objects.create(
            username= username,
            email= email,
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            designation =designation,
            is_lecturer = is_lecturer,
            is_admin = is_admin,
            is_hod = is_hod
    
        )
        password_ = generate_password()
        user.set_password(password_)
        user.save()
        send_password_and_username(username, email, password_)
        messages.success(request, 'User with email address ' + email + ' has been added to the list.')
        return redirect ('accounts:users')
    form = AddUserSignUpForm()
    return render(request,template_name,{'form':form})