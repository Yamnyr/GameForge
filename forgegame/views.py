from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Game


def home(request):
    games = Game.objects.all()
    return render(request, "forgegame/home.html", {"games": games})


@login_required
def dashboard(request):
    games = Game.objects.all()
    return render(request, "forgegame/dashboard.html", {"games": games})


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
            messages.error(request, "Nom d’utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, "forgegame/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après inscription
            return redirect("forgegame:dashboard")
        else:
            messages.error(request, "Erreur lors de l’inscription.")
    else:
        form = UserCreationForm()
    return render(request, "forgegame/signup.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("forgegame:home")


@login_required
def favorites(request):
    games = Game.objects.filter(favorite__user=request.user)
    return render(request, "forgegame/favorites.html", {"games": games})
