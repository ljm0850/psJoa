from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField('email address', blank=True, null=True)
    nickname = models.CharField('nickname',max_length=20,blank=False, null=True)

    def __str__(self):
        return self.username