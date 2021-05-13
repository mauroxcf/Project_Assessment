from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import User, Order, Payment
from .serializers import UserSerializer, OrderSerializer, PaymentSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .methods import MultipleFieldLookupMixin
from rest_framework.response import Response
from django_filters import rest_framework as filters

class OrderFilter(filters.FilterSet):
    start_date = filters.DateFromToRangeFilter(field_name="date", lookup_expr='gte')
    end_date = filters.DateFromToRangeFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['idOrder', 'date', 'city', 'state', 'country']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['^idOrder', '^date', '^city', '^state', '^country']
    ordering_fields = ['date', 'idOrder']
    ordering = ['date']
    filterset_class = OrderFilter

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
