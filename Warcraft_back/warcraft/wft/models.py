from django.contrib.auth.models import User
from django.db import models


class Targets(models.Model):
    name_ru = models.CharField(max_length=255, primary_key=True)
    name_en = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.name_ru


class Image(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(blank=True,default='Нет описания')
    image = models.ImageField(upload_to='images')
    user = models.OneToOneField(User,related_name='image',on_delete=models.CASCADE,null=True,blank=True,unique=True)


    def __str__(self):
        return self.name or self.image.url

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Video(models.Model):
    video = models.FileField(upload_to='videos')
    categories = [
        ('game_video', 'Игровое видео'),
        ('game_process', 'Игровой процесс'),
    ]
    category = models.CharField(max_length=100, choices=categories)
    description = models.TextField(blank=True,default='Нет описания')
    name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.video.url

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Audio(models.Model):
    audio = models.FileField(upload_to='audio')
    name = models.TextField(blank=True, default='Нет названия')
    categories = [
        ('Music', 'Музыка'),
        ('Replays', 'Реплики персонажей'),
        ('Ability_Sound', 'Звук способностей'),
    ]
    category = models.CharField(max_length=100, choices=categories)

    def __str__(self):
        return self.audio.url

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'


class Maps(models.Model):
    campaign_title = models.CharField(max_length=255)
    campaign_subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=255)
    images = models.ManyToManyField(Image, related_name='maps', blank=True)
    videos = models.ManyToManyField(Video, related_name='maps', blank=True)
    file = models.FileField(upload_to='maps')
    description = models.TextField(blank=True,default='Нет описания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


class Locate(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    images = models.ManyToManyField(Image, related_name='locates', blank=True)
    description = models.TextField(blank=True,default='Нет описания')
    videos = models.ManyToManyField(Video, related_name='locates',blank=True)
    main_locate = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_locates', null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class CharacterOrBuild(models.Model):
    DATA = {
    'health':0,
    'mana':0,
    'build_time':0,
    'health_regeneration':0,
    'mana_regeneration':0,
    'gold_cost':0,
    'wood_cost':0,
    'food_cost':0,
    'sight_range_day':0,
    'sight_range_night':0,
    'attack_speed':0,
    'repair_time':0,
    'repair_gold_cost':0,
    'repair_wood_cost':0,
    'attack_area':0,
    'attack_damage_min':0,
    'attack_damage_max':0,
    'movement_speed':0,
    'attack_range':0,
    'defence':0,
    }
    data = models.JSONField(blank=True, default=dict)

    name = models.CharField(max_length=100)
    races = [
        ('Alliance', 'Альянс'),
        ('Horde', 'Орда'),
        ('Undead', 'Нежить'),
        ('NightElves', 'Ночные эльфы'),
        ('Naga', 'Наги'),
        ('NeutralHostile', 'Нейтрально-враждебные'),
        ('NeutralPassive', 'Нейтрально-пассивные'),
        ('NonstandardUnits', 'Нестандартные войска')
    ]
    race = models.CharField(max_length=100, choices=races)
    description = models.TextField(blank=True,default='Нет описания')
    movement_types = [
        ('None', 'Нет'),
        ('Pedestrian', 'Пеший'),
        ('Equestrian', 'Конный'),
        ('Flying', 'Летающий'),
        ('Soaring', 'Парящий'),
        ('Swimming', 'Плывущий'),
        ('Amphibious', 'Земноводный'),
    ]
    movement_type = models.CharField(max_length=100, choices=movement_types)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='characters')
    types_of_attack = [
        ('None', 'Нет'),
        ('Normal', 'Обычная'),
        ('Ranged', 'Дальний бой'),
        ('Artillery', 'Артиллерия'),
        ('Spell', 'Заклинание'),
        ('Dark_Power', 'Сила Тьмы'),
        ('Magic', 'Магическая'),
        ('Hero', 'Герой')

    ]
    type_of_attack = models.CharField(max_length=100, choices=types_of_attack)
    types_of_defence = [
        ('Normal', 'Обычная'),
        ('Light', 'Легкая'),
        ('Medium', 'Средняя'),
        ('Heavy', 'Тяжелая'),
        ('Fortified', 'Укрепленная'),
        ('Hero', 'Герой'),
        ('Divine', 'Божественная'),
        ('No_Protection', 'Без защиты')

    ]
    type_of_defence = models.CharField(max_length=100, choices=types_of_defence)
    attack_targets = models.ManyToManyField(Targets, blank=True)
    is_build = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж или здание'
        verbose_name_plural = 'Персонажи или здания'


class Hero(CharacterOrBuild):
    level = models.PositiveIntegerField(default=10,blank=True)
    HERO_DATA = {
    'intelligence':0,
    'agility':0,
    'strength':0,
    'agility_per_level':0,
    'strength_per_level':0,
    'intelligence_per_level':0,

    }
    hero_data = models.JSONField(blank=True, default=dict)
    primary_attributes = [
        ('strength', 'Сила'),
        ('agility', 'Ловкость'),
        ('intelligence', 'Разум'),
    ]
    primary_attribute = models.CharField(max_length=100, choices=primary_attributes)
    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = 'Герои'


class Upgrade(models.Model):
    NAMES = [
        'name 1',
    ]
    names = models.JSONField(blank=True, default=dict)
    description = models.TextField(blank=True, default='Нет описания')
    levels = models.PositiveIntegerField(default=1, blank=True)
    EFFECTS = {
        'level_1': [
            'Такой-то скилл наносит на 10 больше урона',
        ],
    }
    effects = models.JSONField(blank=True, default=dict)
    wood_cost = models.PositiveIntegerField(default=0)
    gold_cost = models.PositiveIntegerField(default=0)
    image = models.ManyToManyField(Image, related_name='upgrades')
    hotkey = models.CharField(max_length=1)
    character = models.ManyToManyField(CharacterOrBuild, blank=True, related_name='upgrades')

    def __str__(self):
        return self.names[0]

    class Meta:
        verbose_name = 'Улучшение'
        verbose_name_plural = 'Улучшения'


class StarterSkill(models.Model):
    DATA = {
        'cooldown': 0,
        'mana_cost': 0,
        'damage': 0,
        'duration': 0,
        'coverage_area': 0,
        'casting_range': 0,
        'number_of_targets': 1,
        'damage_per_second': 0,
        'mana_cost_per_second': 0,

    }
    data = models.JSONField(blank=True, default=dict)

    name = models.CharField(max_length=255, primary_key=True)
    TYPES = [
        ('passive', 'Пассивный'),
        ('active', 'Активный'),
    ]
    type = models.CharField(max_length=255, choices=TYPES)
    autocast = models.BooleanField(default=False)
    image = models.ManyToManyField(Image, related_name='skills')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    target = models.ManyToManyField(Targets, blank=True, related_name='skills')
    hotkey = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class FinisherSkill(StarterSkill):
    unit = models.ForeignKey(CharacterOrBuild, on_delete=models.CASCADE, null=True, blank=True)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, null=True, blank=True)



class Skill(FinisherSkill):

    needed_upgrades = models.ManyToManyField(Upgrade, blank=True, related_name='skills')
    description = models.TextField(blank=True, default='Нет описания')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

class HeroSkill(FinisherSkill):
    HERO_SKILL_DATA = {
        'cooldown': [0,0],
        'mana_cost': [0,0],
        'damage': [0,0],
        'duration': [0,0],
        'coverage_area': [0,0],
        'casting_range': [0,0],
        'number_of_targets': [1,1],
        'damage_per_second': [0,0],
        'mana_cost_per_second': [0,0],
    }
    levels = models.PositiveIntegerField(default=1, blank=True)
    needed_level = models.PositiveIntegerField(default=1, blank=True)
    needed_next_level = models.PositiveIntegerField(default=2, blank=True)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    DESCRIPTION = [
        'Такой-то скилл наносит 10 урона',
        'Такой-то скилл наносит 20 урона',
    ]
    description = models.JSONField(blank=True,default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык героя'
        verbose_name_plural = 'Навыки героя'

class Item(StarterSkill):
    description = models.TextField(blank=True, default='Нет описания')
    DATA = {
        'cooldown': 0,
        'mana_cost': 0,
        'damage': 0,
        'duration': 0,
        'coverage_area': 0,
        'casting_range': 0,
        'number_of_targets': 1,
        'damage_per_second': 0,
        'mana_cost_per_second': 0,
        'cost':0,
        'recharge_interval': 0, # интервал пополнения
        'level': 1,
        'max_quantity':1,
        'can_be_thrown':False,
        'can_be_purchased_in_shops':False,
        'can_be_sold':False,
        'must_be_activated':False,
        'can_be_depleted':False,
        'durability':75,
    }
    CLASSES = [
        ('permanent', 'Постоянные'),
        ('with_charges', 'Имеющие заряды'),
        ('enhancing', 'Усиливающие'),
        ('artifact', 'Артефакты'),
        ('sellable', 'Подлежащие продаже'),
        ('campaign_only', 'Только для кампании'),
        ('miscellaneous', 'Разные'),
    ]
    classification = models.CharField(max_length=255, choices=CLASSES)


class Constants(models.Model):
    bonus_attack = models.PositiveIntegerField(default=1,blank=True)
    agi_bonus_def = models.PositiveIntegerField(default=0.3,blank=True)
    int_bonus_mana = models.PositiveIntegerField(default=15,blank=True)
    agi_bonus_attack_speed = models.PositiveIntegerField(default=0.02,blank=True)
    str_bonus_health = models.PositiveIntegerField(default=25,blank=True)
    start_def = models.IntegerField(default=-2,blank=True)
    str_bonus_heal = models.PositiveIntegerField(default=0.05,blank=True)
    int_bonus_mana_regen = models.PositiveIntegerField(default=0.05,blank=True)

    hero_gold_cost = models.PositiveIntegerField(default=0.4,blank=True)
    hero_gold_cost_level = models.PositiveIntegerField(default=0.2,blank=True)
    hero_wood_cost = models.PositiveIntegerField(default=0,blank=True)
    hero_wood_cost_level = models.PositiveIntegerField(default=0.2,blank=True)
    hero_gold_cost_moment = models.PositiveIntegerField(default=0.8,blank=True)
    hero_wood_cost_moment = models.PositiveIntegerField(default=0.8,blank=True)
    hero_health_moment = models.PositiveIntegerField(default=0.5,blank=True)

    hero_time_cost = models.PositiveIntegerField(default=65,blank=True)
    hero_time_cost_max = models.PositiveIntegerField(default=200,blank=True)

    bonus_heal_in_austral = models.PositiveIntegerField(default=1.66,blank=True)
    refund_rate = models.PositiveIntegerField(default=0.75,blank=True)
    attack_speed_in_cold = models.PositiveIntegerField(default=-0.25,blank=True)
    move_speed_in_cold = models.PositiveIntegerField(default=-0.5,blank=True)
    day_time = models.PositiveIntegerField(default=480,blank=True)
    chance_to_miss =  models.PositiveIntegerField(default=0.25,blank=True)


    def __str__(self):
        return 'Константы'

    class Meta:
        verbose_name = 'Константы'
        verbose_name_plural = 'Константы'


class Cheats(models.Model):
    data = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return 'Читы'

    class Meta:
        verbose_name = 'Читы'
        verbose_name_plural = 'Читы'