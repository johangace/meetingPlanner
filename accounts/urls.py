
from django.contrib import admin
from django.urls import path

from accounts import views
from django.conf.urls import include, url


urlpatterns = [
    path('login', views.login_user, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('edituser', views.edit_user, name="edituser"),
    path('<username>/friends', views.friends, name="friends"),
    path('<username>/<verb>', views.change_friends, name="change_friends"),
    path('<username>', views.get_user_profile, name='profile'),
]


