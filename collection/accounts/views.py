from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_http_methods, require_GET

from .forms import RegistrationForm


@sensitive_post_parameters("password1", "password2")
@never_cache
@require_http_methods(["GET", "POST"])
def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegistrationForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        user = form.save()  
        login(request, user)  # 建立会话
        return redirect("dashboard")

    return render(request, "accounts/register.html", {"form": form})


@never_cache
@login_required
@require_GET
def dashboard(request):
    return render(request, "accounts/dashboard.html")
