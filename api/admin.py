from django.contrib import admin
from .models import Faculty,Department,Event,Examination,Staff

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Event)
admin.site.register(Examination)
admin.site.register(Staff)