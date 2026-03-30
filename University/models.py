from django.db import models

# Create your models here.

class University(models.Model):
    u_name = models.CharField(max_length=100)
    u_code = models.CharField(max_length=20, unique=True)
    u_city = models.CharField(max_length=100)
    u_state = models.CharField(max_length=100)

    u_email = models.EmailField(unique=True, null=True, blank=True)
    u_contact = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.u_name