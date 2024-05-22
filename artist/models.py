from django.db import models
from user.models import CustomUser

class Artist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"