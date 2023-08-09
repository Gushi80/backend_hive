from django.db import models

# Create your models here.
class User(models.Model):
    class Meta(object):
        db_table="user"
    name=models.CharField(
        'Name', blank=False, null=False, max_length=250
    )
    email=models.CharField(
        'email', blank=False, null=False, max_length=300
    )
    password=models.CharField(
        'password', blank=False, null=False, max_length=100
    )
    token=models.CharField(
        'token', blank=True, null=True, max_length=500, db_index=True
    )
    token_expires=models.DateTimeField(
        'token expiration date', blank=True, null=True
    )
    created_at=models.DateTimeField(
        'Creation Date', blank=True, auto_now_add=True
    )
    updated_at=models.DateTimeField(
        'updation date', blank=True, auto_now_add=True
    )

    def __str__(self):
        return self.email