from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.parsers import FormParser, MultiPartParser


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    parser_classes = (FormParser, MultiPartParser)
    lookup_field = "nip"
