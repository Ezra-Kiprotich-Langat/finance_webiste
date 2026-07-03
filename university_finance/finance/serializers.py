from rest_framework import serializers
from .models import InvoiceModel, PaymentModel

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceModel
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'

