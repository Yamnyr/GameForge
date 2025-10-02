from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Game  # à créer plus tard


def home(request):
    return render(request, "forgegame/home.html")


@login_required
def dashboard(request):
    return render(request, "forgegame/dashboard.html")


@login_required
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "forgegame/game_detail.html", {"game": game})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("forgegame:dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "forgegame/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("forgegame:login")
    else:
        form = UserCreationForm()
    return render(request, "forgegame/signup.html", {"form": form})


@login_required
def favorites(request):
    games = Game.objects.filter(favorite=True, user=request.user)
    return render(request, "forgegame/favorites.html", {"games": games})
