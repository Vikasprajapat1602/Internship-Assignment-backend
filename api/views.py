from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Importing the task for sending welcome emails
from .tasks import send_welcome_email

# Create your views here.

# public API view
@api_view(['GET'])
def public_api(request):
    return Response({"message": "This is a public API."})

# protected API view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": f"Hello {request.user.username}, you are authenticated!"})

# API view that sends a welcome email in the background
@api_view(['GET'])
def public_api(request):
    send_welcome_email.delay("Vikas")
    return Response({"message": "Email will be sent in background!"})
