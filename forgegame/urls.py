from django.urls import path
from . import views

app_name = "forgegame"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("game/<int:pk>/", views.game_detail, name="game_detail"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("favorites/", views.favorites, name="favorites"),
]
