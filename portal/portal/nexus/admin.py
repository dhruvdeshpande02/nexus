# admin.py
from django.contrib import admin
from .models import User,Student,Coordinator,TNPAdmin,Notice

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(TNPAdmin)
admin.site.register(Notice)

