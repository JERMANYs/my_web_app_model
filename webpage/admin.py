from django.contrib import admin

# Register your models here.
from . models import student


@admin . register(student)
class Admin(admin.ModelAdmin):
    list_display = ("std_id","name","prefix" "lastname","phone")
    search_fields = ("std_id","name","prefix","lastname","phone")