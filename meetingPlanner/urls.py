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
from django.urls import path, include
from website.views import welcome, date, about
from accounts.views import login_user, username,  logout_user, register, profile, edit_user
# from meetings.views import detail, room, roomDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome,  name='welcome'),
    path('date', date),
    path('about', about),
    path('meetings/', include('meetings.urls')),
    path('login', login_user, name="login"),
    path('register', register, name="register"),
    path('username', username, name="username"),
    path('logout', logout_user, name="logout"),
    path('profile', profile, name="profile"),
    path('edituser', edit_user, name="edituser"),
]