from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
# from django.forms import modelform_factory
from .forms import MeetingForm

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def room(request):
    return render(request, 'meetings/rooms.html',
                  {"message": " from views.py",
                   "rooms": Room.objects.all()
                   })


def roomDetail(request, id):
    theroom = get_object_or_404(Room, pk=id)
    return render(request, "meetings/roomDetail.html", {"room": theroom})


# MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})


