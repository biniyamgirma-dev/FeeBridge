from django.db import models
from schools.models import School
from accounts.models import User, GenderChoices

class StatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    GRADUATED = "GRADUATED", "Graduated"
    WITHDRAWN = "WITHDRAWN", "Withdrawn"
      
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    grade = models.IntegerField()
    section = models.CharField(max_length=2)
    parent = models.ForeignKey(User, on_delete=models.PROTECT, related_name="children")
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name="students")
    date_of_birth  = models.DateField()
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.ACTIVE) 
    
    def __str__(self):
        return f"Name: {self.full_name} (Parent: {self.parent})"