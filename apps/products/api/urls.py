from django.urls import path

from apps.products.api.viewsets.general_views import MeasureUnitListAPIView,IndicatorListAPIView,CategoryProductListAPIView
from apps.products.api.viewsets.product_views import (
    ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'),    
]