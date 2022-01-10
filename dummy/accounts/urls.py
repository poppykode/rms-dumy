from django.urls import path
from .views import (
    login_view,
    login,
    redirect_logged,
    hod_dashboard,
    users,
    toggle_user_status,
    user_signup,
    user_details,
    admin_dashboard
)

app_name = 'accounts'
urlpatterns = [
    path('login/form', login_view, name='login_view'),
    path('redirect_logged', redirect_logged, name='redirect_logged'),
    path('login', login, name='login'),
    path('dashboard/hod', hod_dashboard, name='hod_dashboard'),
    path('dashboard/admin', admin_dashboard, name='admin_dashboard'),
    path('users', users, name='users'),
    path('toggle/<int:pk>', toggle_user_status, name='toggle_user_status'),
    path('signup', user_signup, name='user_signup'),
    path('user/details/<int:pk>', user_details, name='user_details'),
]
