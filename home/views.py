from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from django.contrib import auth

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

authe = firebase.auth()


def singIn(request):
    return render(request, "SignIn.html")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid cerediantials"
        return render(request, "SignIn.html", {"msg": message})
    print(user)
    request.session['user'] = user
    return render(request, "Welcome.html", {"e": email})


def logout(request):
    auth.logout(request)
    return render(request, 'SignIn.html')


# Create your views here.

def sample(request):
    try:
        user = request.session['user']
    except:
        user=None
    return render(request, "index.html",{'user':user})


def home(request):
    db = firebase.database()
    try:
        user=request.session['user']
        print(user)
    except:
        user=None

    video = db.child("videosnew").get().val()
    videolink = []
    for k, v in video.items():
        videolink.append("https://www.youtube.com/embed/" + video[k]['videoId'])

    users = db.child("users").get()
    return render(request, "youtube_videos.html", {'videolink': videolink})
