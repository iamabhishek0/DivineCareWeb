from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def sample(request):

    return render(request, "index.html")


def home(request):
    return render(request, "youtube_videos.html")
