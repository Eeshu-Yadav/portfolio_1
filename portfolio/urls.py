from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, LegSettingsViewSet, PortfolioProgView

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'legsettings', LegSettingsViewSet)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('prog/', PortfolioProgView.as_view(), name='portfolio-prog'),
    path('portfolios/<int:portfolio_pk>/legsettings/', LegSettingsViewSet.as_view({'get': 'list', 'post': 'create'}), name='legsettings-list'),
    path('portfolios/<int:portfolio_pk>/legsettings/<int:pk>/', LegSettingsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='legsettings-detail'),
]
