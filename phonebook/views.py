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

            # if user authenticated
            phone_no = []
            email_id = []
            for i, key in enumerate (request.POST):
                value = request.POST[key]
                if ('phone_no' in key):
                    print (key + ':' + value)
                    phone_no.append (request.POST.get (key, None))

                if ('email_id' in key):
                    print (key + ':' + value)
                    email_id.append (request.POST.get (key, None))

            name = request.POST.get ('name', None)

            temp_user = User.objects.get (username=request.user)

            usr=names (
                name=name,
                owner=temp_user,
            )
            usr.save()

            # taking object of recently saved name
            # saved_name = names.objects.filter (name=name, owner=temp_user).order_by ('-id')[:1]

            # saving multiple phones
            for j in range (0, len (phone_no), +1):
                phone (
                    names_id=usr,
                    phone_no=phone_no[j],
                ).save ()

            # saving multiple emails
            for k in range (0, len (email_id), +1):
                email (
                    names_id=usr,
                    email_id=email_id[k],
                ).save ()

            response_message = "Contact " + name + " saved!"

            return JsonResponse ({"message": response_message})




        else:
            phone_no=[]
            email_id=[]
            for i,key in enumerate(request.POST):
                value = request.POST[key]
                if('phone_no' in key):
                    print (key+':'+value)
                    phone_no.append (request.POST.get (key, None))

                if ('email_id' in key):
                    print (key + ':' + value)
                    email_id.append (request.POST.get (key, None))


            name = request.POST.get ('name', None)

            temp_user = User.objects.get (username='lol')

            usr=names (
                name=name,
                owner=temp_user,
            )
            usr.save()


            # taking object of recently saved name
            # saved_name = names.objects.filter (name=name, owner=temp_user).order_by ('-id')[:1]

            # saving multiple phones
            for j in range(0, len(phone_no),+1):

                phone (
                    names_id=usr,
                    phone_no=phone_no[j],
                ).save ()

            # saving multiple emails
            for k in range(0, len(email_id),+1):

                email (
                    names_id=usr,
                    email_id=email_id[k],
                ).save ()


            response_message="Contact "+name+" saved!"

            return JsonResponse({"message":response_message})


