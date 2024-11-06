# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TargetsView, ImageViewSet, VideoViewSet, MapsViewSet, LocateView,
    SkillViewSet, HeroSkillViewSet, CharacterOrBuildViewSet, HeroViewSet,
    AudioViewSet, RegisterView, LoginView, ProfileView, LogoutView, UpgradeViewSet,ItemViewSet
)

router = DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'maps', MapsViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'hero-skills', HeroSkillViewSet)
router.register(r'characters-or-builds', CharacterOrBuildViewSet)
router.register(r'heroes', HeroViewSet)
router.register(r'audio', AudioViewSet)
router.register(r'upgrades', UpgradeViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
