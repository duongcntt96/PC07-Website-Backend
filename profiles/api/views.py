from rest_framework.response import Response
from rest_framework import viewsets

from api.paginations import CustomPagination

from profiles.models import Team, UserProfile
from django.contrib.auth.models import User, Group

from .serializers import TeamSerializer, UserProfileSerializer, UserSerializer, GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = CustomPagination


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["ten", "username__username"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomPagination


class RegisterAPIView(APIView):

    def post(self, request):
        from .serializers import UserSerializer
        user = UserSerializer(data=request.data)
        if (user.is_valid()):
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
