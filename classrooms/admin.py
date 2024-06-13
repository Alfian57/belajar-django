from django.contrib import admin
from .models import Classroom


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    search_fields = ["name"]
    readonly_fields = ["slug"]
    list_filter = ["created_at"]


# Register your models here.
admin.site.register(Classroom, ClassroomAdmin)
