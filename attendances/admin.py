from django.contrib import admin
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "status", "created_at"]
    search_fields = ["student__name", "subject__name"]
    list_filter = ["created_at", "status"]


admin.site.register(Attendance, AttendanceAdmin)
