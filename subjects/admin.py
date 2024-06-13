from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    search_fields = ["name"]
    readonly_fields = ["slug"]
    list_filter = ["created_at"]


admin.site.register(Subject, SubjectAdmin)
