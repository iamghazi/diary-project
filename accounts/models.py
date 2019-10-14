from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(unique=True,blank=False)
    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pic', blank=True, null=True)
    bio = models.TextField(max_length=250, default='',blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if(created):
        UserProfile.objects.create(user=instance)

models.signals.post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
