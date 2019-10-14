from django.conf import settings
from django.db import models

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notes', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
