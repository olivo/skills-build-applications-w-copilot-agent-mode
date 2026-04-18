from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captainamerica@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='ironman@marvel.com', activity_type='run', duration=30, date=timezone.now()),
            Activity(user='captainamerica@marvel.com', activity_type='cycle', duration=45, date=timezone.now()),
            Activity(user='spiderman@marvel.com', activity_type='swim', duration=25, date=timezone.now()),
            Activity(user='batman@dc.com', activity_type='run', duration=40, date=timezone.now()),
            Activity(user='superman@dc.com', activity_type='cycle', duration=60, date=timezone.now()),
            Activity(user='wonderwoman@dc.com', activity_type='swim', duration=35, date=timezone.now()),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=100)
        Leaderboard.objects.create(team='dc', points=120)

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Situps', description='Do 30 situps', difficulty='easy'),
            Workout(name='Squats', description='Do 40 squats', difficulty='medium'),
            Workout(name='Burpees', description='Do 15 burpees', difficulty='hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
