from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list=['id','name','roll','city']

# Register your models here.
