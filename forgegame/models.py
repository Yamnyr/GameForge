# games/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

# --------------------------
# Modèle de jeu
# --------------------------
class Game(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='games')
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    ambiance = models.CharField(max_length=100)
    keywords = models.TextField()
    references = models.TextField(blank=True)
    storyline = models.TextField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# --------------------------
# Modèle de personnage
# --------------------------
class Character(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    abilities = models.TextField()
    backstory = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

# --------------------------
# Modèle de lieu
# --------------------------
class Location(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

# --------------------------
# Modèle favoris
# --------------------------
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} likes {self.game.title}"
