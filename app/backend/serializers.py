from rest_framework import serializers
from backend.models import Product

class LeadSerializers(serializers.ModelSerializers):
    class Meta:
        model = Product
        fields = ('id', 'name', 'type')
