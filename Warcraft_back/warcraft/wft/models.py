from django.contrib.auth.models import User
from django.db import models


class Targets(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.name_ru


class Image(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, default='Нет описания')
    image = models.ImageField(upload_to='images')
    user = models.OneToOneField(User, related_name='image', on_delete=models.CASCADE, null=True, blank=True,
                                unique=True)

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
    description = models.TextField(blank=True, default='Нет описания')
    name = models.CharField(max_length=255, null=True, blank=True)

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
    description = models.TextField(blank=True, default='Нет описания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


class Locate(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    images = models.ManyToManyField(Image, related_name='locates', blank=True)
    description = models.TextField(blank=True, default='Нет описания')
    videos = models.ManyToManyField(Video, related_name='locates', blank=True)
    main_locate = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_locates', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


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
    wood_cost_level = models.PositiveIntegerField(default=0)
    gold_cost_level = models.PositiveIntegerField(default=0)
    time_cost = models.PositiveIntegerField(default=0)
    time_cost_level = models.PositiveIntegerField(default=0)

    images = models.ManyToManyField(Image, related_name='upgrades',blank=True)
    hotkey = models.CharField(max_length=1)
    hotkey_ru = models.CharField(max_length=1)
    needed_technologies = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.names[0]

    class Meta:
        verbose_name = 'Улучшение'
        verbose_name_plural = 'Улучшения'


races = [
    ('Alliance', 'Альянс'),  # 0
    ('Horde', 'Орда'),  # 1
    ('Undead', 'Нежить'),  # 2
    ('NightElves', 'Ночные эльфы'),  # 3
    ('Naga', 'Наги'),  # 4
    ('NeutralHostile', 'Нейтрально-враждебные'),  # 5
    ('NeutralPassive', 'Нейтрально-пассивные'),  # 6
    ('NonstandardUnits', 'Нестандартные войска')  # 7
]
movement_types = [
    ('None', 'Нет'),  # 0
    ('Pedestrian', 'Пеший'),  # 1
    ('Equestrian', 'Конный'),  # 2
    ('Flying', 'Летающий'),  # 3
    ('Soaring', 'Парящий'),  # 4
    ('Swimming', 'Плывущий'),  # 5
    ('Amphibious', 'Земноводный'),  # 6
]
types_of_attack = [
    ('None', 'Нет'),  # 0
    ('Normal', 'Обычная'),  # 1
    ('Ranged', 'Дальний бой'),  # 2
    ('Artillery', 'Артиллерия'),  # 3
    ('Spell', 'Заклинание'),  # 4
    ('Dark_Power', 'Сила Тьмы'),  # 5
    ('Magic', 'Магическая'),  # 6
    ('Hero', 'Герой')  # 7

]
types_of_defence = [
    ('Normal', 'Обычная'),  # 0
    ('Light', 'Легкая'),  # 1
    ('Medium', 'Средняя'),  # 2
    ('Heavy', 'Тяжелая'),  # 3
    ('Fortified', 'Укрепленная'),  # 4
    ('Hero', 'Герой'),  # 5
    ('Divine', 'Божественная'),  # 6
    ('No_Protection', 'Без защиты')  # 7

]
health_regeneration_types = [
    ('None', 'Нет'),  # 0
    ('Always', 'Всегда'),  # 1
    ('only_on_corrupted_land', 'Только на порченой земле'),  # 2
    ('only_day', 'Только днем'),  # 3
    ('only_night', 'Только ночью'),  # 4
]

TYPES = [
    ('passive', 'Пассивный'),
    ('active', 'Активный'),
]


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

    type = models.CharField(max_length=255, choices=TYPES)
    autocast = models.BooleanField(default=False)
    image = models.ManyToManyField(Image, related_name='skills')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    hotkey = models.CharField(max_length=1)
    hotkey_ru = models.CharField(max_length=1)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class FinisherSkill(StarterSkill):
    target = models.ManyToManyField(Targets, blank=True, related_name='skills')
    is_hero_skill = models.BooleanField(default=False)


class Skill(FinisherSkill):
    needed_upgrades = models.ManyToManyField(Upgrade, blank=True, related_name='skills')
    needed_technologies = models.JSONField(default=dict, blank=True)
    description = models.TextField(blank=True, default='Нет описания')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class HeroSkill(FinisherSkill):
    HERO_SKILL_DATA = {
        'cooldown': [0, 0],
        'mana_cost': [0, 0],
        'damage': [0, 0],
        'duration': [0, 0],
        'coverage_area': [0, 0],
        'casting_range': [0, 0],
        'number_of_targets': [1, 1],
        'damage_per_second': [0, 0],
        'mana_cost_per_second': [0, 0],
    }
    levels = models.PositiveIntegerField(default=1, blank=True)
    needed_level = models.PositiveIntegerField(default=1, blank=True)
    needed_next_level = models.PositiveIntegerField(default=2, blank=True)
    DESCRIPTION = [
        'Такой-то скилл наносит 10 урона',
        'Такой-то скилл наносит 20 урона',
    ]
    description = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык героя'
        verbose_name_plural = 'Навыки героя'


class CharacterOrBuild(models.Model):
    data = models.JSONField(blank=True, default=dict)
    model = models.FileField(blank=True, null=True, upload_to='models')
    type_unit = models.ManyToManyField(Targets, related_name='char', blank=True)
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100, choices=races)
    description = models.TextField(blank=True, default='Нет описания')
    movement_type = models.CharField(max_length=100, choices=movement_types)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='characters')
    type_of_defence = models.CharField(max_length=100, choices=types_of_defence)
    is_build = models.BooleanField(default=False, blank=True)
    is_hero = models.BooleanField(default=False, blank=True)
    can_build = models.BooleanField(default=False, blank=True)
    can_train = models.BooleanField(default=False, blank=True)
    chars_builds = models.ManyToManyField('self', blank=True, related_name='sub_chars_builds')
    health_regeneration_time = models.CharField(max_length=100, choices=health_regeneration_types)
    hotkey = models.CharField(max_length=1)
    hotkey_ru = models.CharField(max_length=1)
    tip = models.CharField(max_length=255)
    characters = models.ManyToManyField(Upgrade, blank=True, related_name='upgrades')
    skills = models.ManyToManyField(Skill, blank=True, related_name='char')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Персонаж или здание'
        verbose_name_plural = 'Персонажи или здания'


primary_attributes = [
    ('strength', 'Сила'),
    ('agility', 'Ловкость'),
    ('intelligence', 'Разум'),
]


class Hero(CharacterOrBuild):
    primary_attribute = models.CharField(max_length=100, choices=primary_attributes)
    second_name = models.CharField(max_length=255)
    hero_skills = models.ManyToManyField(HeroSkill, blank=True, related_name='heroes')

    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = 'Герои'


CLASSES = [
    ('permanent', 'Постоянные'),
    ('with_charges', 'Имеющие заряды'),
    ('enhancing', 'Усиливающие'),
    ('artifact', 'Артефакты'),
    ('sellable', 'Подлежащие продаже'),
    ('campaign_only', 'Только для кампании'),
    ('miscellaneous', 'Разные'),
]


class Item(StarterSkill):
    description = models.TextField(blank=True, default='Нет описания')
    abilities = models.ManyToManyField(Skill, blank=True, related_name='items')
    classification = models.CharField(max_length=255, choices=CLASSES)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Constants(models.Model):
    bonus_attack = models.PositiveIntegerField(default=1, blank=True)

    agi_bonus_def = models.PositiveIntegerField(default=0.3, blank=True)
    agi_bonus_attack_speed = models.PositiveIntegerField(default=0.02, blank=True)

    str_bonus_health = models.PositiveIntegerField(default=25, blank=True)
    str_bonus_heal = models.PositiveIntegerField(default=0.05, blank=True)

    int_bonus_mana = models.PositiveIntegerField(default=15, blank=True)
    int_bonus_mana_regen = models.PositiveIntegerField(default=0.05, blank=True)

    start_def = models.IntegerField(default=-2, blank=True)
    hero_gold_cost = models.PositiveIntegerField(default=0.4, blank=True)
    hero_gold_cost_level = models.PositiveIntegerField(default=0.2, blank=True)
    hero_wood_cost = models.PositiveIntegerField(default=0, blank=True)
    hero_wood_cost_level = models.PositiveIntegerField(default=0.2, blank=True)
    hero_gold_cost_moment = models.PositiveIntegerField(default=0.8, blank=True)
    hero_wood_cost_moment = models.PositiveIntegerField(default=0.8, blank=True)
    hero_health_moment = models.PositiveIntegerField(default=0.5, blank=True)

    hero_time_cost = models.PositiveIntegerField(default=0.65, blank=True)
    hero_time_cost_max = models.PositiveIntegerField(default=2, blank=True)

    bonus_heal_in_austral = models.PositiveIntegerField(default=1.66, blank=True)
    # cancel build or upgrade_build
    refund_rate = models.PositiveIntegerField(default=0.75, blank=True)
    attack_speed_in_cold = models.PositiveIntegerField(default=-0.25, blank=True)
    move_speed_in_cold = models.PositiveIntegerField(default=-0.5, blank=True)
    day_time = models.PositiveIntegerField(default=480, blank=True)
    chance_to_miss = models.PositiveIntegerField(default=0.25, blank=True)

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
