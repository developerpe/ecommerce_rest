from apps.expense_manager.models import Supplier
from rest_framework import status

from tests.test_setup import TestSetUp
from tests.factories.expense_manager.expense_factories import SupplierFactory

class ExpenseTestCase(TestSetUp):
    url = '/expense/expense/'

    def test_search_supplier(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + 'search_supplier/',
            {
                'ruc_or_business_name': supplier.ruc
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ruc'], supplier.ruc)
    
    def test_search_supplier_error(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + 'search_supplier/',
            {
                'ruc_or_business_name': '43543543'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(supplier.ruc, '43543543')
        self.assertEqual(response.data['mensaje'], 'No se ha encontrado un Proveedor.')

    def test_new_supplier(self):
        supplier = SupplierFactory().build_supplier_JSON()
        response = self.client.post(
            self.url + 'new_suplier/',
            supplier,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.all().count(), 1)
        self.assertEqual(response.data['supplier']['ruc'], supplier['ruc'])