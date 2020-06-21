from django.shortcuts import render

from .models import Myself


def index(request):
    text = Myself.objects.get(id=1)
    return render(request, 'about_myself/about_myself.html', {'text': text})
