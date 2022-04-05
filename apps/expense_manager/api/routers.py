from rest_framework.routers import DefaultRouter

from apps.expense_manager.api.viewsets.expense_viewsets import ExpenseViewSet

router = DefaultRouter()

router.register(r'expense', ExpenseViewSet, basename='expense')

urlpatterns = router.urls