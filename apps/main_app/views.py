from django.shortcuts import render, redirect


#-----this is need but not right now -----#
# from .forms import *
# from .models import *
# from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'main_app/homepage.html', {})
