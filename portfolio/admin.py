from django.contrib import admin

# Register your models here.
from .models import Contact,Blogs

admin.site.register(Contact)
admin.site.register(Blogs)