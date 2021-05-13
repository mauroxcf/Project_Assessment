from django.urls import path
from . import views
from rest_framework import routers

app_name = 'app'
router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='users')
router.register('order', views.OrderViewSet, basename='order')
router.register('payment', views.PaymentViewSet, basename='payment')

urlpatterns = router.urls
