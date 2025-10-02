from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game  # à créer plus tard si nécessaire


def home(request):
    return render(request, "forgegame/home.html")


@login_required
def dashboard(request):
    return render(request, "forgegame/dashboard.html")


@login_required
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)  # Game doit exister dans models.py
    return render(request, "forgegame/game_detail.html", {"game": game})
