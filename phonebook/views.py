from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import names, phone, email
from .serializers import names_serializer, phone_serializer, email_serializer, contacts_serializer

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.

class contacts(APIView):

    def get(self, request):

        if request.user.is_authenticated ():
            current_user=request.user
            name = names.objects.filter (owner=current_user)
            for i in range (0, len (name)):
                phon = phone.objects.filter (names_id=name[i].id)
                name.phones = phon
                emil = email.objects.filter (names_id=name[i].id)
                name.emails = emil

            contact_serial = contacts_serializer (name, many=True)
            # print(contact_serial)
            # print(contact_serial.data)
            return Response (contact_serial.data)

        else:
            # current_user=request.user
            name = names.objects.all()
            for i in range (0, len (name)):
                phon = phone.objects.filter (names_id=name[i].id)
                name.phones = phon
                emil = email.objects.filter (names_id=name[i].id)
                name.emails = emil

            contact_serial = contacts_serializer (name, many=True)
            # print(contact_serial)
            # print(contact_serial.data)
            return Response (contact_serial.data)



    def post(self, request):
        if request.user.is_authenticated ():
            name = request.POST.get ('name', None)
            phone_no = request.POST.get ('phone_no', None)
            email_id = request.POST.get ('email_id', None)

            names (
                name=name,
                owner=request.user,
            ).save ()

            # taking object of recently saved name
            saved_name = names.objects.get(name=name, owner=request.user).order_by('-id').first(1)

            phone(
                names_id=saved_name.id,
                phone_no=phone_no,
            ).save()

            email (
                names_id=saved_name.id,
                email_id=email_id,
            ).save ()

            # sending saved response
            name=saved_name
            for i in range (0, len (name)):
                phon = phone.objects.filter (names_id=name[i].id)
                name.phones = phon
                emil = email.objects.filter (names_id=name[i].id)
                name.emails = emil

            contact_serial = contacts_serializer (name, many=True)
            # print(contact_serial)
            # print(contact_serial.data)
            return Response (contact_serial.data)


        else:
            name = request.POST.get ('name', None)
            phone_no = request.POST.get ('phone_no', None)
            email_id = request.POST.get ('email_id', None)

            temp_user = User.objects.get (username='lol')

            names (
                name=name,
                owner=temp_user,
            ).save ()

            # taking object of recently saved name
            saved_name = names.objects.get (name=name, owner=temp_user).order_by ('-id').first (1)

            phone (
                names_id=saved_name.id,
                phone_no=phone_no,
            ).save ()

            email (
                names_id=saved_name.id,
                email_id=email_id,
            ).save ()

            # sending saved response
            name = saved_name
            for i in range (0, len (name)):
                phon = phone.objects.filter (names_id=name[i].id)
                name.phones = phon
                emil = email.objects.filter (names_id=name[i].id)
                name.emails = emil

            contact_serial = contacts_serializer (name, many=True)
            # print(contact_serial)
            # print(contact_serial.data)
            return Response (contact_serial.data)



