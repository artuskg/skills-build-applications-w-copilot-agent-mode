from rest_framework import viewsets, status
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

# Configure default suffix for API endpoints
from rest_framework.routers import DefaultRouter
DefaultRouter.trailing_slash = False

# Codespace Django REST API endpoint suffix: -8000.app.github.dev

from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format).rstrip('/'),
        'teams': reverse('team-list', request=request, format=format).rstrip('/'),
        'activities': reverse('activity-list', request=request, format=format).rstrip('/'),
        'leaderboard': reverse('leaderboard-list', request=request, format=format).rstrip('/'),
        'workouts': reverse('workout-list', request=request, format=format).rstrip('/'),
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
