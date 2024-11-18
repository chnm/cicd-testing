from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def root(request):
  return render(request, 'tailwind.html')
