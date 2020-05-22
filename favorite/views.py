from django.shortcuts import render
from .models import Channel

# Create your views here.

def home(request):
    channels = Channel.objects
    return render(request, 'home.html', {'channels':channels})