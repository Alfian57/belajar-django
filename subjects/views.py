from rest_framework import viewsets
from .models import Subject
from .serializers import SubjectSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated


@extend_schema(request=SubjectSerializer)
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthenticated,)
