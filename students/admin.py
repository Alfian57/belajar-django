from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["nisn", "name", "gender", "created_at"]
    search_fields = ["name", "nisn"]
    list_filter = ["created_at", "gender"]


admin.site.register(Student, StudentAdmin)
