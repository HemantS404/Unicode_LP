from django.urls import path, include
import signup_handler.views as views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('', views.login_user, name = 'login'),
    path('accounts/login/', views.login_user, name = 'login'),
    path('accounts/signup', views.signup_user, name = 'signup'),
    path('accounts/logout', views.logout_user, name = 'logout'),
    path('accounts/passwordreset', PasswordChangeView.as_view(), name = 'passwordreset')
]