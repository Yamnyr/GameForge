from django.contrib import admin
from .models import Game, Character, Location, Favorite

# --------------------------
# Inlines pour Game
# --------------------------
class CharacterInline(admin.TabularInline):
    model = Character
    extra = 1

class LocationInline(admin.TabularInline):
    model = Location
    extra = 1

# --------------------------
# Admin Game
# --------------------------
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'user', 'is_public', 'created_at')
    search_fields = ('title', 'genre', 'user__username')
    list_filter = ('genre', 'is_public', 'created_at')
    inlines = [CharacterInline, LocationInline]

# --------------------------
# Admin Favorite
# --------------------------
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'created_at')
    search_fields = ('user__username', 'game__title')

# --------------------------
# Enregistrement des modèles
# --------------------------
admin.site.register(Game, GameAdmin)
admin.site.register(Character)
admin.site.register(Location)
admin.site.register(Favorite, FavoriteAdmin)
