from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Targets, Image, Video, Maps, Locate, Skill, HeroSkill, CharacterOrBuild, Hero, Audio, Upgrade, Item


class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maps
        fields = '__all__'

class LocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locate
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class HeroSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSkill
        fields = '__all__'

class CharacterOrBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterOrBuild
        fields = '__all__'

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgrade
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)