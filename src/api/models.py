from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True ,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

    @property
    def owner(self):
        return self.email
   

class UserProfile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    Name        = models.CharField(max_length=255)
    Language    = models.CharField(max_length=20)
    PhoneNum    = models.CharField(max_length=20)
    Currency    = models.CharField(max_length=5)
    
