from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

from .decorators import addTimeStamp
from .models import Profile
from django.contrib.auth.decorators import login_required


# from django.dispatch import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if username == "":
            return HttpResponse('no Username')
        if password == "":
            return HttpResponse('no Password')
        if email == "":
            return HttpResponse('no Email')
        # if username.exists or email.exists:
        #     return HttpResponse('email or username exists')
        User.objects.create_user(username=username, password=password, email=email)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Unauthorized!!!')
        else:
            login(request, user)
            return redirect("welcome")

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if username == "": return HttpResponse('no Username')
        if password == "": return HttpResponse('no Password')
        if user is None: return HttpResponse('Unauthorized!!!')
        login(request, user)
        return redirect("welcome")
    return render(request, 'login.html')


@login_required(login_url="/login")
def username(request):
    return HttpResponse(' Your username is : ' + request.user.username + "Your Phone:" + request.userprofile.phone)


@login_required(login_url="/login")
def profile(request):
    return render(request, 'profile.html', {"profile": Profile.objects.all()})


# @addTimeStamp
@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    return HttpResponse("Successfully logged out")


@login_required(login_url="/login")
def edit_user(request):
    if request.method == "POST":
        user = request.user
        phone = request.POST['phone']
        info = request.POST['info']
        profile, created = Profile.objects.get_or_create(user=request.user)
        user.profile.phone = phone
        user.profile.info = info
        user.save()
    return render(request, 'edituser.html')
