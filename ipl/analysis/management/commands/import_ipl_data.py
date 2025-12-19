import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from analysis.models import Team, Match, Delivery


class Command(BaseCommand):
    help = 'Import IPL dataset'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.import_matches()
            self.import_deliveries()

    def import_matches(self):
        with open('data/matches.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                team1, _ = Team.objects.get_or_create(name=row['team1'])
                team2, _ = Team.objects.get_or_create(name=row['team2'])
                winner = None
                if row['winner']:
                    winner, _ = Team.objects.get_or_create(name=row['winner'])

                Match.objects.create(
                    id=row['id'],
                    season=row['season'],
                    team1=team1,
                    team2=team2,
                    winner=winner
                )

    def import_deliveries(self):
        with open('data/deliveries.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Delivery.objects.create(
                    match_id=row['match_id'],
                    batting_team=Team.objects.get(name=row['batting_team']),
                    bowling_team=Team.objects.get(name=row['bowling_team']),
                    over=row['over'],
                    ball=row['ball'],
                    total_runs=row['total_runs'],
                    extra_runs=row['extra_runs']
                )
