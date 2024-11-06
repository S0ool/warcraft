from django.contrib import admin
from .models import Targets, Image, Video, Maps, Locate, Skill, HeroSkill, CharacterOrBuild, Hero, Audio,Upgrade,Item

lst = [Targets, Image, Video, Maps, Locate, Skill, HeroSkill, CharacterOrBuild, Hero, Audio,Upgrade,Item]

admin.site.register(lst)



