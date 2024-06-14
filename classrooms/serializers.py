from rest_framework import serializers
from .models import Classroom
from rest_framework import serializers


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"
        extra_kwargs = {"slug": {"read_only": True}}
