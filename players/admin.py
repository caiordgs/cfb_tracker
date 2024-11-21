from django.contrib import admin
from .models import Player, Stat

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'team', 'overall', 'games_played', 'snaps')

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = (
        'player', 'season', 'games_started', 'passing_yards', 'longest_pass',
        'sacks_taken', 'touchdowns_passed', 'interceptions', 'rushing_yards',
        'fumbles', 'broken_tackles', 'YAC', 'receiving_yards', 'touchdowns'
    )
    list_filter = ('season', 'player__team')
