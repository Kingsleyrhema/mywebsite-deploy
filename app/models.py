from django.db import models

class viewer(models.Model):
    email = models.CharField(max_length=20)
    def __str__(self):
        return self.email
# Create your models here.
