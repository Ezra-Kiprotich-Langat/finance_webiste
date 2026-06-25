from django.db import models
from students.models import StudentProfileModel
from academics.models import UnitModel

class AttendanceRecordModel(models.Model):
    student = models.ForeignKey(StudentProfileModel, on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitModel, on_delete=models.CASCADE)
    total_classes = models.PositiveBigIntegerField(default=0)
    attended_classes = models.PositiveBigIntegerField(default=0)

    def percentage(self):
        if self.total_classes == 0:
            return 0
        return (self.attended_classes / self.total_classes) * 100
    
    def exam_eligible(self):
        return self.percentage >= 75