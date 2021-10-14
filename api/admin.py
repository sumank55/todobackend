from django.contrib import admin
from .models import Plan

# Register your models here.
@admin.register(Plan)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id','items']
