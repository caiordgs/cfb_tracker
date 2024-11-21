from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Season(models.Model):
    year = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    touchdowns = models.IntegerField(default=0)
    yards = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.name} - {self.year}"
