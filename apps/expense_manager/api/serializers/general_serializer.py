from rest_framework import serializers

from apps.expense_manager.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('id', 'ruc', 'business_name', 'address')