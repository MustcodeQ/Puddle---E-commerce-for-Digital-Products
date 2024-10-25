# community/views.py

from django.shortcuts import render
from django.conf import settings

def main(request):
    print("Template directories:", settings.TEMPLATES[0]['DIRS'])
    return render(request, 'community/main.html')