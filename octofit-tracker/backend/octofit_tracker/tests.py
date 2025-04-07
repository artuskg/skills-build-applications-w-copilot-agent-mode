from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

class TeamTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='teammember',
            email='member@example.com',
            password='testpass123'
        )
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.members.count(), 1)
        self.assertEqual(self.team.members.first(), self.user)

class ActivityTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='activityuser',
            email='activity@example.com',
            password='testpass123'
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration=timedelta(minutes=30)
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, timedelta(minutes=30))

class LeaderboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='leaderuser',
            email='leader@example.com',
            password='testpass123'
        )
        self.leaderboard = Leaderboard.objects.create(
            user=self.user,
            score=100
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user, self.user)
        self.assertEqual(self.leaderboard.score, 100)

class WorkoutTests(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout description',
            difficulty='Medium',
            duration=timedelta(minutes=45)
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.description, 'A test workout description')
        self.assertEqual(self.workout.difficulty, 'Medium')
        self.assertEqual(self.workout.duration, timedelta(minutes=45))
