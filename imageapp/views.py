from django.shortcuts import render

from rest_framework import viewsets,filters,permissions,generics
from .serializers import ItemSerializer
from .models import Item

# Create your views here.
class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemDetailView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
