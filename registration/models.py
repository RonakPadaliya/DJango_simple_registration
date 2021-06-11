from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    mob = models.CharField(max_length=10)