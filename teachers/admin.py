from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["nip", "name", "email", "gender"]
    search_fields = ["name", "nip"]
    list_filter = ["created_at", "gender"]


admin.site.register(Teacher, TeacherAdmin)
