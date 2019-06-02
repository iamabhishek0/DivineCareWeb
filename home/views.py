from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyB4LuASCKc3QxocENU6T16hRGQu6gTILT4",
    'authDomain': "divinecareapp-2ec91.firebaseapp.com",
    'databaseURL': "https://divinecareapp-2ec91.firebaseio.com",
    'projectId': "divinecareapp-2ec91",
    'storageBucket': "divinecareapp-2ec91.appspot.com",
    'messagingSenderId': "142556288828",
    'appId': "1:142556288828:web:9614f8f60904601f"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# Create your views here.

def sample(request):
    return render(request, "index.html")


def home(request):
    db = firebase.database()
    video = db.child("videosnew").get().val()
    videolink = []
    for k, v in video.items():
        videolink.append("https://www.youtube.com/embed/" + video[k]['videoId'])

    users = db.child("users").get()
    return render(request, "youtube_videos.html", {'videolink': videolink})
