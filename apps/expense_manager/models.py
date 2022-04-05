from django.db import models

from apps.base.models import BaseModel
from apps.products.models import Product

class Supplier(BaseModel):
    ruc = models.CharField(unique=True, max_length=11)
    business_name = models.CharField('Razón Social', unique=True, max_length=150, null=False, blank=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'   

    def __str__(self):
        return self.business_name

    def to_dict(self):
        return {
            'id': self.id,
            'ruc': self.ruc,
            'business_name': self.business_name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }

class PaymentType(BaseModel):
    name = models.CharField('Nombre de Medio de Pago', max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Medio de Pago'
        verbose_name_plural = 'Medio de Pagos'

    def __str__(self):
        return self.name


class Voucher(BaseModel):
    name = models.CharField('Nombre de comprobante de Pago', max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Comprobante'
        verbose_name_plural = 'Comprobantes'

    def __str__(self):
        return self.name


class ExpenseCategory(BaseModel):
    name = models.CharField('Nombre de Categoría de Gasto', max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Categoria de Gasto'
        verbose_name_plural = 'Categorias de Gastos'

    def __str__(self):
        return self.name

class Expense(BaseModel):
    date = models.DateField('Fecha de emisión de factura', auto_now=False, auto_now_add=False)    
    quantity = models.DecimalField('Cantidad', max_digits=10, decimal_places=2)
    unit_price = models.DecimalField('Precio Unitario', max_digits=10, decimal_places=2, default=0)
    voucher_number = models.CharField('Número de comprobante', max_length=50)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'

    def __str__(self):
        return self.voucher_number

class Merma(BaseModel):
    date = models.DateField('Fecha de emisión de Merma', auto_now=False, auto_now_add=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField('Cantidad', max_digits=7, decimal_places=2)
    lost_money = models.DecimalField('Dinero perdido', max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['id']
        verbose_name = 'Merma'
        verbose_name_plural = 'Mermas'


    def __str__(self):
        return "Merma de {0}".format(self.product.__str__())