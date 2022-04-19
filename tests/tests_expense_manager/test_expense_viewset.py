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