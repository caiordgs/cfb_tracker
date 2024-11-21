from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=10,
        choices=[
            ('QB', 'Quarterback'),
            ('RB', 'Running Back'),
            ('WR', 'Wide Receiver'),
            ('TE', 'Tight End'),
            ('LT', 'Left Tackle'),
            ('LG', 'Left Guard'),
            ('C', 'Center'),
            ('RG', 'Right Guard'),
            ('RT', 'Right Tackle'),
            ('LE', 'Left End'),
            ('RE', 'Right End'),
            ('DT', 'Defensive Tackle'),
            ('LOLB', 'Left Outside Linebacker'),
            ('MLB', 'Middle Linebacker'),
            ('ROLB', 'Right Outside Linebacker'),
            ('CB', 'Cornerback'),
            ('FS', 'Free Safety'),
            ('SS', 'Strong Safety'),
            ('K', 'Kicker'),
            ('P', 'Punter'),
        ]
    )
    team = models.CharField(max_length=100)
    overall = models.IntegerField()
    games_played = models.IntegerField(default=0)
    snaps = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.position})"

class Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='stats')
    season = models.CharField(max_length=4)  # Ano da temporada
    games_started = models.IntegerField(default=0)
    passing_attempts = models.IntegerField(default=0)
    passing_completions = models.IntegerField(default=0)
    passing_yards = models.IntegerField(default=0)
    longest_pass = models.IntegerField(default=0)
    sacks_taken = models.IntegerField(default=0)
    touchdowns_passed = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    rushing_attempts = models.IntegerField(default=0)
    rushing_yards = models.IntegerField(default=0)
    fumbles = models.IntegerField(default=0)
    broken_tackles = models.IntegerField(default=0)
    YAC = models.IntegerField(default=0)
    rushing_long = models.IntegerField(default=0)
    twenty_yard_rushes = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)
    receiving_yards = models.IntegerField(default=0)
    touchdowns = models.IntegerField(default=0)
    receiving_long = models.IntegerField(default=0)
    drops = models.IntegerField(default=0)

    def completion_percentage(self):
        if self.passing_attempts > 0:
            return round((self.passing_completions / self.passing_attempts) * 100, 2)
        return 0.0

    def qb_rating(self):
        if self.passing_attempts > 0:
            return round(
                (
                    (8.4 * self.passing_yards) +
                    (330 * self.touchdowns_passed) +
                    (100 * self.passing_completions) -
                    (200 * self.interceptions)
                ) / self.passing_attempts,
                2
            )
        return 0.0

    def __str__(self):
        return f"Stats for {self.player.name} - {self.season}"

class Record(models.Model):
    category = models.CharField(max_length=100)  # Categoria do recorde (ex.: "Jardas de Passe")
    value = models.IntegerField()  # Valor do recorde
    holder = models.CharField(max_length=100, null=True, blank=True)  # Nome do detentor do recorde
    team = models.CharField(max_length=100, null=True, blank=True)  # Time ou escola relacionada

    def __str__(self):
        return f"{self.category} - {self.value} ({self.holder})"

class HistoricRecord(models.Model):
    school = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    year_start = models.IntegerField(null=True, blank=True)
    year_end = models.IntegerField(null=True, blank=True)
    completions = models.IntegerField(null=True, blank=True)
    attempts = models.IntegerField(null=True, blank=True)
    completion_percentage = models.FloatField(null=True, blank=True)
    yards = models.IntegerField(null=True, blank=True)
    yards_per_attempt = models.FloatField(null=True, blank=True)
    touchdowns = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    passer_rating = models.FloatField(null=True, blank=True)
    rush_attempts = models.IntegerField(null=True, blank=True)
    rush_yards = models.IntegerField(null=True, blank=True)
    yards_per_carry = models.FloatField(null=True, blank=True)
    rush_tds = models.IntegerField(null=True, blank=True)
    receptions = models.IntegerField(null=True, blank=True)
    receiving_yards = models.IntegerField(null=True, blank=True)
    yards_per_catch = models.FloatField(null=True, blank=True)
    receiving_tds = models.IntegerField(null=True, blank=True)
    plays_from_scrim = models.IntegerField(null=True, blank=True)
    yards_from_scrim = models.IntegerField(null=True, blank=True)
    avg_yards_per_play = models.FloatField(null=True, blank=True)
    scrimmage_tds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.player} ({self.school})"
