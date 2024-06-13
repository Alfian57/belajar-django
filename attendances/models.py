from django.db import models
import uuid


class Attendance(models.Model):
    class AttendanceStatus(models.TextChoices):
        PRESENT = "P", "Present"
        ABSENT = "A", "Absent"
        PERMISSION = "I", "Permission"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    subject = models.ForeignKey("subjects.Subject", on_delete=models.CASCADE)
    status = models.CharField(choices=AttendanceStatus.choices, max_length=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"
