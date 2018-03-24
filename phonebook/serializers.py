

from rest_framework import serializers
from .models import names, phone, email

class names_serializer(serializers.ModelSerializer):
    class Meta:
        model=names
        fields='__all__'
        # fields=('ticker', 'volume')

class phone_serializer(serializers.ModelSerializer):
    class Meta:
        model=phone
        fields='__all__'
        # fields=('phone_no', 'status')

class email_serializer(serializers.ModelSerializer):
    class Meta:
        model=email
        fields='__all__'
        # fields=('ticker', 'volume')


