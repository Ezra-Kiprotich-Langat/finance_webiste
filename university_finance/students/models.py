from django.db import models
from django.contrib.auth.models import User

class StudentProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    programme = models.CharField(max_length=100)
    year_of_study = models.PositiveBigIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __set__(self):
        return self.registration_number



