from django.contrib import admin
from .models import names, phone, email

admin.site.register(names,phone,email)

