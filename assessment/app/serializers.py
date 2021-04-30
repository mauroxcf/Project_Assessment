from .models import User, Order, payment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'
