from crypt import methods
from os import stat
from django.db.models import Q

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.expense_manager.models import Supplier

from apps.expense_manager.api.serializers.general_serializer import SupplierSerializer
from apps.expense_manager.api.serializers.expense_serializer import *

class ExpenseViewSet(viewsets.GenericViewSet):
    serializer_class = ExpenseSerializer

    @action(methods=['get'], detail=False)
    def search_supplier(self, request):
        ruc_or_business_name = request.query_params.get('ruc_or_business_name', '')
        supplier = Supplier.objects.filter(
            Q(ruc__iexact=ruc_or_business_name)|
            Q(business_name__iexact=ruc_or_business_name)
        ).first()
        if supplier:
            supplier_serializer = SupplierSerializer(supplier)
            return Response(supplier_serializer.data, status=status.HTTP_200_OK)
        return Response({
            'mensaje': 'No se ha encontrado un Proveedor.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['post'], detail=False)
    def new_suplier(self ,request):
        data_supplier = request.data
        data_supplier = SupplierRegisterSerializer(data=data_supplier)
        if data_supplier.is_valid():
            data_supplier = data_supplier.save()
            return Response({
                'message:': 'Proveedor registrado correctamente!',
                'supplier': data_supplier
            }, status=status.HTTP_201_CREATED)
        return Response({'error': data_supplier.errors}, status=status.HTTP_400_BAD_REQUEST)