from django.db import models
from datetime import time
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    floorNumber = models.IntegerField(default=1)
    roomNumber = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} at {self.roomNumber}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} by {self.created_by}"
