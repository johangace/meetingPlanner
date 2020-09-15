from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
# from django.forms import modelform_factory
from .forms import MeetingForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import User
from .serializers import MeetingSerializer, RoomSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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


class ListRoom(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


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


# class ListMeeting(generics.ListCreateAPIView):
#     queryset = Meeting.objects.all()
#     serializer_class = MeetingSerializer


# class DetailMeeting(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Meeting.objects.all()
#     serializer_class = MeetingSerializer


@api_view(['GET', 'POST'])
def ListMeeting(request):
    if request.method == 'GET':
        data = Meeting.objects.all()
        serializer = MeetingSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
def DetailMeeting(request, meeting_id):
    try:
        meeting = get_object_or_404(Meeting, pk=meeting_id)
    except Meeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = get_object_or_404(Meeting, pk=meeting_id)
        serializer = MeetingSerializer(
            data, context={'request': request}, many=False)
        return Response(serializer.data)
        # serializer = MeetingSerializer(
        #     meeting, context={'request': request}, many=False)
        # return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MeetingSerializer(
            meeting, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
