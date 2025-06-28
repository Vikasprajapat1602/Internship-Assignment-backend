from django.db import models

# Create your models here.

class TelegramUser(models.Model):
   username = models.CharField(max_length=255, unique=True)

   def __str__(self):
      return self.username