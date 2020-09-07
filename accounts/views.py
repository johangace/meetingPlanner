from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .decorators import addTimeStamp
from .models import Profile, Friend
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
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    getFriendsOf = Friend.objects.get(current_user=request.user)
    owner = request.user.profile
    friends_list = getFriendsOf.user.all()
    is_friend = getFriendsOf.user.filter(username=user).exists()
    return render(request, 'profile.html', {'isFriend': is_friend, "owner": owner, "friend": getFriendsOf, "userProfile": user, "friends":  friends_list})


# def is_friend(request, username):
#     user = User.objects.get(username=username)
#     friend = Friend.objects.get(current_user=user)
#     return friend.user.filter(username=username).exists()

# @addTimeStamp
@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    # return HttpResponse("Successfully logged out")
    # return render(request, 'login.html')
    return redirect("welcome")


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


@login_required
def change_friends(request, username, verb):

    new_friend = User.objects.get(username=username)
    owner = request.user.profile
    if verb == 'add':
        Friend.make_friend(request.user, new_friend)
    else:
        Friend.delete_friend(request.user, new_friend)
    # return redirect("welcome")
    return redirect("profile", new_friend)


@login_required(login_url="/login")
def friends(request, username):
    user = User.objects.get(username=username)
    friend = Friend.objects.get(current_user=user)
    friends_list = friend.user.all()
    return render(request, 'friends.html', {"friends": friends_list,  "userProfile": user})


