from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import names, phone, email
from .serializers import names_serializer, phone_serializer, email_serializer

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.

class names_list(APIView):

    def get(self, request):

        if request.user.is_authenticated ():
            pass
        else:
            pass


        # current_user=request.user
        name = names.objects.filter(owner=1)
        serializer = names_serializer (name)
        print(serializer)
        print(serializer.data)
        return Response (serializer.data)


