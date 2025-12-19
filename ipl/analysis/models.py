from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Match(models.Model):

    season = models.IntegerField()
    team1 = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team1_matches')
    team2 = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team2_matches')
    winner = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=True,
        related_name='wins')

    def __str__(self):
        return f"{self.season}-Match{self.id}"


class Delivery(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    batting_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="batting_deliveries")
    bowling_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="bowling_deliveries")
    over = models.IntegerField()
    ball = models.IntegerField()
    total_runs = models.IntegerField()
    extra_runs = models.IntegerField()
