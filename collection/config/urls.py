from django.contrib import admin
from django.urls import include, path
from evaluations import views

urlpatterns = [
    path('', include('accounts.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
