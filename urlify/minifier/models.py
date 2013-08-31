from django.db import models


class MinifiedURL(models.Model):
    url = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

