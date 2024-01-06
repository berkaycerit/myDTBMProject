"""
URL configuration for myDTBMProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 
from .views import ogrenci_delete, ogrenci_create, ogrenciye_ders_atama


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('lessons/', views.lessons, name='lessons'),
    path('students/', views.students, name='students'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:ogrenci_id>/delete/', ogrenci_delete, name='ogrenci_delete'),
    path('students/create/', ogrenci_create, name='ogrenci_create'),
    path('students/<int:ogrenci_id>/ders-atama/', ogrenciye_ders_atama, name='ogrenciye_ders_atama'),

    path('admin/', admin.site.urls),
]
