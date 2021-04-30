from .models import User, Order, payment
from .serializers import UserSerializer, OrderSerializer, paymentSerializer
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class paymentViewSet(viewsets.ModelViewSet):
    queryset = payment.objects.all()
    serializer_class = paymentSerializer
