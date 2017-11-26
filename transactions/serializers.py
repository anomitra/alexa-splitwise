from rest_framework import serializers
from transactions import models


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        read_only_fields = (
            'id',
        )
        fields = (
            'id',
            'amount',
            'date',
            'description',
            'user',
        )
