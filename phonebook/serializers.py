

from rest_framework import serializers
from .models import names, phone, email

class names_serializer(serializers.ModelSerializer):
    class Meta:
        model=names
        fields='__all__'
        # fields=('name', 'status', 'phones','emails','created_at', 'owner')

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

class contacts_serializer(serializers.ModelSerializer):
    phones=phone_serializer(source='phone_set', many=True, required=False)
    emails=email_serializer(source='email_set', many=True, required=False)

    class Meta:
        model=names
        # depth=1
        # fields='__all__'
        fields=('name', 'status', 'phones','emails','created_at', 'owner')
