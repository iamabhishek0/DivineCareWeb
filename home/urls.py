from django.urls import path
from home import views

urlpatterns = [
    path('', views.sample, name="home"),
    path('home/', views.home, name="home1"),
    path('signin/', views.singIn, name="home2"),
    path('postsign/', views.postsign, name="home3"),
    path('logout/', views.logout, name="log"),
]
