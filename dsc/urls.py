"""dsc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url

from admissions.views import prep_cohort, core_cohort, student_profile, student_background
from outcomes.views import student_post

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^users/prep_cohorts$', prep_cohort, name='users'),
    url(r'^users/core_cohorts$', core_cohort, name='users'),
    url(r'^users/student_profile$', student_profile, name='student_profile'),
    url(r'^users/student_background$', student_background, name='student_background'),
    url(r'^users/student_post$', student_post, name='student_post')
]
