from django.urls import path,include
from .views import VendorListCreate, PurchaseOrderListCreate,VendorPerformanceRetrieve,RegisterUser,PurchaseOrderAcknowledgeViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework_nested import routers
from rest_framework.authtoken import views


router =routers.DefaultRouter()
router.register("vendors",VendorListCreate,basename='vendors')
router.register("purchase_orders",PurchaseOrderListCreate)
router.register(r'purchase_orders/(?P<po_id>\d+)/acknowledge', PurchaseOrderAcknowledgeViewSet, basename='purchase_order_acknowledge')


vendor_performance_router = routers.NestedDefaultRouter(router, r'vendors', lookup='vendor')
vendor_performance_router.register(r'performance', VendorPerformanceRetrieve, basename='vendor_performance')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(vendor_performance_router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/',RegisterUser.as_view())

]