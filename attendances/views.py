from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer


@extend_schema(request=AttendanceSerializer)
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    lookup_field = "id"
