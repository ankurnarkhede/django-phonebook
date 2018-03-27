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

# copied

from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator

# other imports
import time


# rest views start

class api_contacts(APIView):

    def get(self, request):

        print ('1. inside contacts get')

        if request.user.is_authenticated ():
            current_user=request.user
            name = names.objects.filter (owner=current_user).order_by('name')
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
            name = names.objects.all().order_by('name')
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

            print('2. inside contacts post')

            # if user authenticated
            phone_no = []
            email_id = []
            for i, key in enumerate (request.POST):
                value = request.POST[key]
                if ('phone_no' in key):
                    phone_no.append (request.POST.get (key, None))

                if ('email_id' in key):
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
                    phone_no.append (request.POST.get (key, None))

                if ('email_id' in key):
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



# rest views end


# template views start

class UserFormView(View):

    form_class=UserForm
    template_name='auth.html'

    # display blank form
    def get(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect(reverse ('index'))
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})


    # process form data
    def post(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect(reverse ('index'))
        form=self.form_class(request.POST)


        if form.is_valid():

            user=form.save(commit=False)

            # cleaned normalized data
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user=authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    # return redirect('music:index')
                    return HttpResponseRedirect (reverse ('index'))

        # return render (request, self.template_name, {'form': form})
        return HttpResponseRedirect (reverse ('login_user'))


class LoginView(View):
    form_class = UserForm
    template_name = 'auth.html'

    # display blank form
    def get(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect(reverse ('index'))
            # return render (request, "index.html")
        form = self.form_class (None)
        return render (request, self.template_name, {'form': form})


    def post(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect(reverse ('index'))
            # return render (request, "index.html")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect (reverse ('index'))
                # return render (request, "index.html")
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect (reverse ('login_user'))




class LogoutView(View):
    def get(self, request):
        logout(request)
        # form = UserForm (request.POST or None)
        # context = {
        #     "form": form,
        # }
        return HttpResponseRedirect (reverse ('login_user'))


class Home(View):

    def get(self, request):
        if request.user.is_authenticated ():
            return render (request, "index.html",{'current_time': time.time()})
        else:
            return HttpResponseRedirect (reverse ('login_user'))

    # process form data
    def post(self, request):
       pass




class contacts(APIView):

    def get(self, request):

        print ('1. inside contacts get')

        if request.user.is_authenticated ():
            current_user=request.user
            name = names.objects.filter (owner=current_user).order_by('name')
            for i in range (0, len (name)):
                phon = phone.objects.filter (names_id=name[i].id)
                name.phones = phon
                emil = email.objects.filter (names_id=name[i].id)
                name.emails = emil

            print(name)

            contact_serial = contacts_serializer (name, many=True)
            # print(contact_serial)
            # print(contact_serial.data)
            # return Response (contact_serial.data)
            return render (request, "contacts-view.html",{'current_time': time.time(), 'names':name })


        else:
            # current_user=request.user
            name = names.objects.all().order_by('name')
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

            print('2. inside contacts post')

            # if user authenticated
            phone_no = []
            email_id = []
            for i, key in enumerate (request.POST):
                value = request.POST[key]
                if ('phone_no' in key):
                    phone_no.append (request.POST.get (key, None))

                if ('email_id' in key):
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
            print(response_message)

            params={'msg':response_message}

            # return JsonResponse ({"message": response_message})
            # return HttpResponseRedirect (reverse ('index'))
            return render (request, "index.html",{'current_time': time.time(), 'msg': response_message})




        else:
            phone_no=[]
            email_id=[]
            for i,key in enumerate(request.POST):
                value = request.POST[key]
                if('phone_no' in key):
                    phone_no.append (request.POST.get (key, None))

                if ('email_id' in key):
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






































