from rest_framework.routers import DefaultRouter
from apps.products.api.viewsets.general_views import *
from apps.products.api.viewsets.product_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'products',ProductViewSet,basename = 'products')
router.register(r'measure-unit',MeasureUnitViewSet,basename = 'measure_unit')
router.register(r'indicators',IndicatorViewSet,basename = 'indicators')
router.register(r'category-products',CategoryProductViewSet,basename = 'category_products')

urlpatterns = router.urls