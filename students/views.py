from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(request=StudentSerializer)
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "nisn"
