from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Game, Character, Location, Favorite

# --------------------------
# CustomUser
# --------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'avatar')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'avatar')}),
    )

# --------------------------
# Autres modèles
# --------------------------
class CharacterInline(admin.TabularInline):
    model = Character
    extra = 1

class LocationInline(admin.TabularInline):
    model = Location
    extra = 1

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'user', 'is_public', 'created_at')
    search_fields = ('title', 'genre', 'user__username')
    list_filter = ('genre', 'is_public', 'created_at')
    inlines = [CharacterInline, LocationInline]

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'created_at')
    search_fields = ('user__username', 'game__title')

# --------------------------
# Enregistre les modèles
# --------------------------
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Character)
admin.site.register(Location)
admin.site.register(Favorite, FavoriteAdmin)
