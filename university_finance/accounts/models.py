from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
        ('FINANCE', 'Finance'),
        ('REGISTRAR', 'Registar'),
        ('LECTURER', 'Lecturer')
    ]
class UserModel(AbstractUser):
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} {self.role}"