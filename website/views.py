from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room


def welcome(request):
    return render(request, 'website/welcome.html',
                  {"message": " from views.py",
                   "meetings": Meeting.objects.all(),
                   # "rooms": Room.objects.all()
                   })


def date(request):
    return HttpResponse('this page was served at ' + str(datetime.now()))


def about(request):
    return HttpResponse('this is me')
