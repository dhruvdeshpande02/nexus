# admin.py
from django.contrib import admin
from .models import User,Student,Coordinator,TNPAdmin

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(TNPAdmin)

