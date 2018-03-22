from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class names(models.Model):
    name=models.CharField(max_length=100, null=True)
    owner=models.ForeignKey(User)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class phone(models.Model):
    names_id=models.ForeignKey(names)
    phone_no=models.CharField(max_length=20, null=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.phone_no

class email(models.Model):
    names_id=models.ForeignKey(names)
    email_id=models.CharField(max_length=100, null=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email_id




