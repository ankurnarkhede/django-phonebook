from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import names, phone, email
from .serializers import names_serializer, phone_serializer, email_serializer

# Create your views here.
