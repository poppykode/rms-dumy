from django.urls import path
from .views import (
    login_view,
    login,
    redirect_logged,
    admin_dashboard,
    users
)

app_name = 'accounts'
urlpatterns = [
    path('login/form', login_view, name='login_view'),
    path('redirect_logged', redirect_logged, name='redirect_logged'),
    path('login', login, name='login'),
    path('dashboard/admin', admin_dashboard, name='admin_dashboard'),
    path('users', users, name='users'),
 
]
