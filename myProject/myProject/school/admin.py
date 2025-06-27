from django.contrib import admin
from .models import CustomUser, Attendance

admin.site.register(CustomUser)
admin.site.register(Attendance)
