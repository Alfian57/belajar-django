from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

fields = list(UserAdmin.fieldsets)
fields[1] = ("Personal info", {"fields": ("name", "email")})


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = fields
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "gender",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    list_display = ("email", "name", "is_staff")
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
