from django.db import models
from students.models import StudentProfileModel
from academics.models import SemesterModel


class InvoiceModel(models.Model):
    student = models.ForeignKey(StudentProfileModel, on_delete=models.CASCADE)
    semester = models.ForeignKey(SemesterModel, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} {self.amount_due}"


class PaymentModel(models.Model):
    invoice = models.ForeignKey(InvoiceModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference