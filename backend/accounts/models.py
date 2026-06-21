from django.db import models
from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):
    PARENT = "PARENT", "Parent"
    STAFF = "STAFF", "Staff"
    ADMIN = "ADMIN", "Admin"

class GenderChoices(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    role = models.CharField(max_length=20, choices=RoleChoices.choices, default=RoleChoices.PARENT)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"