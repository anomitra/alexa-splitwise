from rest_framework import serializers
from transactions import models


class TransactionSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):

        intent = data.get('request').get('intent').get('name')
        if intent == 'AddCharge':
            import pdb;
            pdb.set_trace()
            slots = data.get('request').get('intent').get('slots')
            amount = slots.get('amount').get('value', 0)
            name = slots.get('user').get('value')
            return {
                'amount': amount,
                'user': name,
                'description': 'Test Description'
            }
        return data

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
