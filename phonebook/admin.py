from django.contrib import admin
from .models import names, phone, email

admin.site.register(names)
admin.site.register(phone)
admin.site.register(email)

