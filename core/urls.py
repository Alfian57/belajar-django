from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from classrooms.views import ClassroomViewSet
from subjects.views import SubjectViewSet
from teachers.views import TeacherViewSet
from students.views import StudentViewSet
from attendances.views import AttendanceViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r"api/classrooms", ClassroomViewSet)
router.register(r"api/subjects", SubjectViewSet)
router.register(r"api/teachers", TeacherViewSet)
router.register(r"api/students", StudentViewSet)
router.register(r"api/attendances", AttendanceViewSet)


urlpatterns = [
    # JWT Token Authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Swagger API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Admin Panel
    path("admin/", admin.site.urls),
]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
