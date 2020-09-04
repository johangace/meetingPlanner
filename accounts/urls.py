
from django.contrib import admin
from django.urls import path
from . import views
from accounts import views


urlpatterns = [
    path('login', views.login_user, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('<int:id>', views.username, name="username"),
    path('<int:id>/profile', views.profile, name="profile"),
    path('edituser', views.edit_user, name="edituser"),
    path('<int:id>/friends', views.friends, name="friend"),
    path('<int:pk>/<verb>', views.change_friends, name="change_friends"),
]


