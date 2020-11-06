from django.shortcuts import render
from rest_framework import viewsets, permissions
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        data = self.request.query_params
        query = Order.objects.all()
        
        if 'from_customer' in data:
            query = Order.objects.filter(customer__username__iexact=data.get('from_customer'))
        
        return query