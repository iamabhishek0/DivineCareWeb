from django.urls import path
from home import views

urlpatterns = [
    path('', views.sample, name="home"),
    path('home/', views.home, name="home1"),
]
