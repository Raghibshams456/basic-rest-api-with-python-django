from rest_framework import serializers
from .models import employee
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        #fields=("firstname")
        fields="__all__"
