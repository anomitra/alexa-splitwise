from transactions import serializers
from transactions import models

from rest_framework.viewsets import ModelViewSet


class TransactionViewSet(ModelViewSet):

    queryset = models.Transaction.objects.all()
    model = models.Transaction
    serializer_class = serializers.TransactionSerializer
