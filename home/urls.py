from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index, name="home"),
    path("home/", views.index, name="home"),
    path("about/", views.about, name="About"),
    path("services/", views.services, name="Services"),
    path('login/',views.loginUser, name="login"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
]
