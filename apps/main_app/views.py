from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from main_app.models import EndUser, TourGuide, Moderator

#-----this is need but not right now -----#
# from .forms import *
# from .models import *
# from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'main_app/homepage.html', {})


def get_user_ip(request):
    pass


def contact(request):
    pass


def login_user(request):
    myErrors = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            if not username:
                myErrors["empty_username"] = "please enter username"
            elif not password:
                myErrors["empty_password"] = "please enter password"
            elif user is None:
                myErrors["invalid"] = "Username and password do not match"
    return render (request, "main_app/login.html", myErrors)


def logout_user(request):
    logout(request)
    return redirect("homepage")


def signup_user(request):
    if request.method == "POST":
        # form validation, save new user object, authenticate and login user
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            modList = request.POST.getlist("make_moderator")
            if modList:
                moderator = Moderator(user=request.user, is_moderator=True)
                moderator.save()
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "main_app/signup.html", {"form": form})
