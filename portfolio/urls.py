from django.contrib import admin
from django.urls import path,include
from .views import home_page,about,contact,blog,Resume_skills

urlpatterns = [
path('',home_page,name='apphome'),
path('about/',about,name='about'),
path('contact/',contact,name='contact'),
path('blog/',blog,name='blog'),
path('resume/',Resume_skills,name='resume'),
] 