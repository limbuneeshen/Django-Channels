from django import urls
from django.urls import path
from .import views

urlpatterns = [
    path('',views.chat,name="index"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.Login,name="login"),
]