
from django.urls import path
from .views import *
urlpatterns = [
    path('', homepage, name='homepage'),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path("signup/", signup_user, name="signup_user"),

]
