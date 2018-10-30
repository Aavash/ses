from django.contrib import admin
from .models.administrator import Administrator
from .models.student import Student


admin.site.register(Administrator)
admin.site.register(Student)
