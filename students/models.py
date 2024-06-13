from django.db import models
from django.core.validators import RegexValidator
import uuid


class Student(models.Model):
    nisn_validator = RegexValidator(
        regex=r"^\d{10}$", message="NISN must consist of 10 digits"
    )

    class GenderChoice(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nisn = models.CharField(max_length=10, unique=True, validators=[nisn_validator])
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GenderChoice.choices, max_length=1)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to="students", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.nisn}"
