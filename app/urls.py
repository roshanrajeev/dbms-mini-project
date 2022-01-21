from django.urls import path, include
from .views import (
    home,
    login,
    logout,
    register,
    profile,
    add_question,
    vote_view,
    view_question,
    add_answer,
    # downvote,
)

urlpatterns = [
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("profile/<int:id>/", profile, name="profile"),
    # path("profile/<int:id>/", profile, name="profile"),
    path("questions/add/", add_question, name="add_question"),
    path("questions/<int:id>/", view_question, name="view_question"),
    path("questions/<int:id>/add_answer/", add_answer, name="add_answer"),
    path("vote/<int:id>/", vote_view, name="vote"),
    # path("downvote/<int:id>/", downvote, name="downvote"),
]
