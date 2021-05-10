from .models import User, Order, Payment
from .serializers import UserSerializer, OrderSerializer, PaymentSerializer
from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from django.db.models import Q
import operator
from functools import reduce
""" this module is only for build other funcionalities """

class MultipleFieldLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[self.lookup_field]
        q = reduce(operator.or_, (Q(x) for x in filter.items()))
        return get_object_or_404(queryset, q)
