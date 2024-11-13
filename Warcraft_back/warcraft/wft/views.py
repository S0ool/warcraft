from django.contrib.auth import authenticate, logout
from django.views.generic import ListView
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Targets, Image, Video, Maps, Locate, Skill, HeroSkill, CharacterOrBuild, Hero, Audio,Upgrade,Item
from .serializers import (
    TargetsSerializer, ImageSerializer, VideoSerializer, MapsSerializer,
    LocateSerializer, SkillSerializer, HeroSkillSerializer, CharacterOrBuildSerializer,
    HeroSerializer, AudioSerializer, UserSerializer, RegisterSerializer,UpgradeSerializer,ItemSerializer
)
from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from rest_framework import viewsets

class AdminOrReadOnlyPermission(IsAdminUser):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return super().has_permission(request, view)


class ImageViewSet(viewsets.ModelViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class VideoViewSet(viewsets.ModelViewSet):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MapsViewSet(viewsets.ModelViewSet):

    queryset = Maps.objects.all()
    serializer_class = MapsSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HeroSkillViewSet(viewsets.ModelViewSet):

    queryset = HeroSkill.objects.all()
    serializer_class = HeroSkillSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CharacterOrBuildViewSet(viewsets.ModelViewSet):

    queryset = CharacterOrBuild.objects.filter(is_hero=False)
    serializer_class = CharacterOrBuildSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HeroViewSet(viewsets.ModelViewSet):

    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AudioViewSet(viewsets.ModelViewSet):

    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpgradeViewSet(viewsets.ModelViewSet):

    queryset = Upgrade.objects.all()
    serializer_class = UpgradeSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AdminOrReadOnlyPermission]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TargetsView(ListAPIView):
    queryset = Targets.objects.all()
    serializer_class = TargetsSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocateView(ListAPIView):
    queryset = Locate.objects.all()
    serializer_class = LocateSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Вы успешно вышли из системы"}, status=status.HTTP_200_OK)




class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'is_superuser': user.is_superuser
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print(1)
        if user is not None:
            print(2)

            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'is_superuser': user.is_superuser

            }, status=status.HTTP_200_OK)
        print(3)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        image = Image.objects.filter(user=request.user).first()
        if image:
            avatar = image.image.url
        else:
            avatar = None
        return Response({"user": serializer.data, "avatar": avatar}, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Пользователь не авторизован"}, status=status.HTTP_401_UNAUTHORIZED)
        image = Image.objects.filter(user=request.user).first()
        if image:
            image.image = request.FILES['avatar']
            image.save()
        else:
            image = Image(
                user=request.user,
            )
            image.image = request.FILES['avatar']
            image.save()
        print("Аватарка успешно обновлена")
        return Response({"message": "Аватарка успешно обновлена"})

