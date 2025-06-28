from django.contrib import admin
# # Importing the TelegramUser model to register it in the admin site
from .models import TelegramUser

# Register your models here.

admin.site.register(TelegramUser)
