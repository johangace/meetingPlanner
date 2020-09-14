"""meetingPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from meetings.views import detail, room, roomDetail, deleteMeeting
from . import views
from website.views import welcome, date, about


from . import views


urlpatterns = [
    # path('<int:id>', views.detail, name="meetingDetail"),
    # path('delete/<meeting_id>', views.deleteMeeting, name="deleteMeeting"),
    # path('rooms', views.room, name="rooms"),
    # path('rooms/<int:id>', views.roomDetail, name="roomDetail"),
    # path('new', views.new, name="new"),


    # # testing API
    # path('roomapi/<int:pk>/', views.DetailRoom.as_view()),
    # path('roomapi', views.ListRoom.as_view()),
    # re_path('meetingapi/<int:pk>/', views.DetailMeeting),

    # re_path('api', views.ListMeeting),

    re_path(r'^meetings/$', views.ListMeeting),
    re_path(r'^api/students/([0-9])$', views.DetailMeeting)
]
