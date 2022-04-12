from django.shortcuts import render, redirect


#-----this is need but not right now -----#
# from .forms import *
# from .models import *
# from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'main_app/homepage.html', {})


def sign_up_user(request):
    pass


def sign_up_guide(request):
    pass


def logout(request):
    pass


def login(request):
    pass


def get_user_ip(request):
    pass


def contact(request):
    pass

def edit_user(request):
    pass
