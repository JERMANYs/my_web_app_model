from django.contrib import admin

# Register your models here.
from . models import student,major


@admin . register(student)
class Admin(admin.ModelAdmin):
    list_display = ("std_id","prefix","name", "lastname","phone","major")
    search_fields = ("std_id","name","lastname","phone")

@admin . register(major)
class Adminmajor(admin.ModelAdmin) :
    list_display = ("name",)