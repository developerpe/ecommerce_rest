from django.db.models import Q

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.base.utils import format_date
from apps.products.models import Product
from apps.expense_manager.models import (
    Supplier, Voucher, PaymentType
)

from apps.expense_manager.api.serializers.general_serializer import *
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

    @action(methods=['get'], detail=False)
    def get_vouchers(self, request):
        data = Voucher.objects.filter(state=True).order_by('id')
        data = VoucherSerializer(data, many=True).data
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_payment_types(self, request):
        data = PaymentType.objects.filter(state=True).order_by('id')
        data = PaymentTypeSerializer(data, many=True).data
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_products(self, request):
        data = Product.objects.filter(state=True).order_by('id')
        data = ProductSerializer(data, many=True).data
        return Response(data)

    def format_data(self, data):
        JWT_authenticator = JWTAuthentication()
        # decode token
        user, _ = JWT_authenticator.authenticate(self.request)
        data['user'] = user.id
        data['date'] = format_date(data['date'])
        return data

    def create(self, request):
        data = self.format_data(request.data)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Factura registrada correctamente.'
                }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message': 'Han ocurrido errores en la creación.',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
