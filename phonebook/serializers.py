

from rest_framework import serializers
from .models import url

class url_serializer(serializers.ModelSerializer):
    class Meta:
        model=url
        fields='__all__'
        # fields=('ticker', 'volume')


