"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeview),
    path('hrmanager/', views.hrmanagerview),
    path('employee/', views.employeeview),
    path('addemp/', views.addempview),
    path('empdata/', views.empdataview),
    path('addnews/', views.addnewsview),
    path('addnewcal/', views.addnewcalview),
    path('jobopening/', views.jobopeningview),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete/<int:id>/', views.deleteview),
    path('update/<int:id>/', views.updateview),
    path('calenderholiday/', views.calenderholidayview),
    path('latestnews/', views.latestnewsview),
    path('jobdetails/',views.jobdetailsview),
    path('latestnews/delete/<int:id>/', views.latestnewsdeleteview),
    path('latestnews/update/<int:id>/', views.latestnewsupdateview),
    path('thanks/', views.thanksview),
    path('getdata/',views.getdataview),
    path('logout/', views.logoutview),
    path('register/', views.userview),
 
]
