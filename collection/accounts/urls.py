from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import StudentLoginForm
from . import views


urlpatterns = [
    path("register/", views.register, name="register"),
    # 复用框架提供的密码验证、登录会话和安全跳转逻辑。
    path("login/", LoginView.as_view(
        template_name="accounts/login.html",
        authentication_form=StudentLoginForm,
        redirect_authenticated_user=True,
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
