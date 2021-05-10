from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import User, Order, Payment
from .serializers import UserSerializer, OrderSerializer, PaymentSerializer
from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from .methods import MultipleFieldLookupMixin
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['idOrder', 'date']
    search_fields = ['=idOrder', 'date']
    ordering_fields = ['date', 'idOrder']
    ordering = ['date']
    """ lookup_fields = ('pk', 'date') """

class OrderVsSpec(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Order, date=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Order.objects.all()

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
