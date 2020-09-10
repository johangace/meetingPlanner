from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
# from django.forms import modelform_factory
from .forms import MeetingForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import User
from .serializers import MeetingSerializer, RoomSerializer
from rest_framework import generics


def isStaffUser(user):
    return user.username == "johan"


@login_required(login_url="/login")
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized")
    return render(request, "meetings/detail.html", {"meeting": meeting})


@login_required(login_url="/login")
def deleteMeeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    meeting.delete()
    return redirect("welcome")


# @user_passes_test(isStaffUser, login_url="/login")
@login_required(login_url="/login")
# @permission_required(perm="meeting.add_meeting", login_url="/login" )
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})


@login_required(login_url="/login")
def room(request):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized")
    return render(request, 'meetings/rooms.html',
                  {"message": " from views.py",
                   "rooms": Room.objects.all()
                   })


@login_required(login_url="/login")
def roomDetail(request, id):
    theroom = get_object_or_404(Room, pk=id)
    return render(request, "meetings/roomDetail.html", {"room": theroom})


class DetailRoom(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListRoom(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListMeeting(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class DetailMeeting(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

# MeetingForm = modelform_factory(Meeting, exclude=[])
