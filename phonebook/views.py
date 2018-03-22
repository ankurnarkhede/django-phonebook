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
        current_user=1
        print('Current User is ',current_user)
        user_phonebook=names.objects.get(owner=current_user)
        serializer=names_serializer(user_phonebook)
        return Response(serializer.data)



