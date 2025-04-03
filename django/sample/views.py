from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from allauth.socialaccount.models import SocialApp

def root(request):
  print(SocialApp.objects.values())
  return render(request, 'tailwind.html')
