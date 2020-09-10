from rest_framework import serializers
from .models import Room, Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'date',
            'start_time',
            'duration',
            'room',
            'created_by'

        )
        model = Meeting


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'floorNumber',
            'roomNumber'
        )
        model = Room
