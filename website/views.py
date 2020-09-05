from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room
from accounts.models import Profile, Friend
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url="accounts/login")
def welcome(request):
    return render(request, 'website/welcome.html',
                  {"message": " from views.py",
                   "meetings": Meeting.objects.all(),
                   # "rooms": Room.objects.all()
                   })


def base(request, username):
    user = User.objects.get(username=username)

    return render(request, 'website/base.html',
                  {"message": " from views.py",
                   "meetings": Meeting.objects.all(),
                   "friends": Friend.objects.all(),

                   })

def date(request):
    return HttpResponse('this page was served at ' + str(datetime.now()))


def about(request):
    return HttpResponse('this is me')


