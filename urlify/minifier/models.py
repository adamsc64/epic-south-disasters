from django.db import models


class MinifiedURL(models.Model):
    submitter = models.ForeignKey('auth.user', null=True)
    url = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
