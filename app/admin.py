from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group','status']
    search_fields = ['name', 'status']
    list_per_page = 10

