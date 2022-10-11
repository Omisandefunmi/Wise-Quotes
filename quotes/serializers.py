from rest_framework import serializers
from .models import *


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['message', 'author', 'source']