from rest_framework import serializers
from .models import Loan
from customers.models import Customer

class LoanSerializer(serializers.ModelSerializer):
    customers = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        many=True
    )
    
    class Meta:
        model = Loan
        fields = '__all__'
    
    def validate_customers(self, value):
        if len(value) > 3:
            raise serializers.ValidationError("A loan cannot have more than 3 customers.")
        elif len(value) == 0:
            raise serializers.ValidationError("A loan must have at least one customer.")
        return value
