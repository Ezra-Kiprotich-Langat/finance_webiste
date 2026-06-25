from django.db import models
from students.models import StudentProfileModel

class SemesterModel(models.Model):
    name = models.CharField(max_length=15)
    is_current = models.BooleanField(default=True)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class UnitModel(models.Model):
    code = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.code} {self.title}"
    
class UnitRegistrationModel(models.Model):
    student = models.ForeignKey(StudentProfileModel, on_delete=models.CASCADE)
    semester = models.ForeignKey(SemesterModel, on_delete=models.CASCADE)
    units = models.ManyToManyField(UnitModel)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} {self.semester}"