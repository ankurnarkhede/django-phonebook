from django.db import models

class names(models.Model):
    name=models.CharField(max_length=100, null=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class phone(models.Model):
    names_id=models.ForeignKey('names')
    # names_id=models.CharField(max_length=20, null=True)
    phone_no=models.CharField(max_length=20, null=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.phone_no

class email(models.Model):
    names_id=models.ForeignKey('names')
    email_id=models.CharField(max_length=100, null=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email_id




