from rest_framework import viewsets
from .models import Classroom
from .serializers import ClassroomSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(request=ClassroomSerializer)
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    lookup_field = "slug"
