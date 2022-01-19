from django.urls import path, include
from .views import home, login, logout, register, profile, add_question, view_question

urlpatterns = [
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("questions/add/", add_question, name="add_question"),
    path("questions/<int:id>/", view_question, name="view_question")
]
