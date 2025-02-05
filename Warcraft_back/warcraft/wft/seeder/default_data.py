from django.core.files.base import File

from .load_from_dir import import_files_from_folder, get_file
from ..models import *
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_dir, 'images')
chars_dir = os.path.join(images_dir, 'chars')
# TODO добавить все данные, распределить по файлам и проверить корректность
targets = [
    ('Airborne', 'Воздушные'),  # 0
    ('PlayerUnits', 'Войска игрока'),  # 1
    ('Enemies', 'Враги'),  # 2
    ('Heroes', 'Герои'),  # 3
    ('Decorations', 'Декорации'),  # 4
    ('Woods', 'Деревья'),  # 5
    ('Trees', 'Древа'),  # 6
    ('Friends', 'Друзья'),  # 7
    ('Spirits', 'Духи'),  # 8
    ('Living', 'Живые'),  # 9
    ('Buildings', 'Здания'),  # 10
    ('Dead', 'Мертвые'),  # 11
    ('Mechanisms', 'Механизмы'),  # 12
    ('Bridges', 'Мосты'),  # 13
    ('Ground', 'Наземные'),  # 14
    ('NotTrees', 'Не древа'),  # 15
    ('NotHeroes', 'Не герои'),  # 16
    ('NotWarrior', 'Не сам воин'),  # 17
    ('NotSuicidal', 'Не самоубийцы'),  # 18
    ('Neutral', 'Нейтральные'),  # 19
    ('None', 'Нет'),  # 20
    ('Invulnerable', 'Неуязвимые'),  # 21
    ('Organisms', 'Организмы'),  # 22
    ('Items', 'Предметы'),  # 23
    ('Others', 'Прочее'),  # 24
    ('Relief', 'Рельеф'),  # 25
    ('Warrior', 'Сам воин'),  # 26
    ('Suicidal', 'Самоубийцы'),  # 27
    ('Allies', 'Союзники'),  # 28
    ('Walls', 'Стены'),  # 29
    ('Vulnerable', 'Уязвимые')  # 30
]
videos = {
    'Исход Орды: Пророчество': r'videos\TutorialIn.mp4',
    'Исход Орды: Сон Тралла': r'videos\TutorialOp.mp4',
    'Падение Лордерона: Предупреждение': r'videos\HumanOp.mp4',
    'Падение Лордерона: Предательство Артеса': r'videos\HumanEd.mp4',
    'Путь Проклятых: Разрушение Даларана': r'videos\UndeadEd.mp4',
    'Вторжение на Калимдор: Гибель Задиры': r'videos\OrcEd.mp4',
    'Конец Вечности': r'videos\NightElfEd.mp4',
    'Ужас из Глубин - Пробуждение': r'videos\IntroX.mp4',
    'Повелитель Тьмы - Финал Время настало': r'videos\Arthas_vs_Ilidan.mp4',
    'Повелитель Тьмы - Ролик: Восхождение': r'videos\OutroX.mp4',
}
game_videos = {
    'Как установить и запустить Warcraft 3 на Windows 10?': r'videos\game_process\download.mp4',
    '⚡ Warcraft 3 Frozen Throne⚡Часть 1⚡Кампания Ночных Эльфов⚡Глава первая⚡Наги⚡': r'videos\game_process\part_1.mp4',
}
cheats = {
    'WhosYourDaddy': 'Запуск «Режима Бога» (убийства с одного удара, юниты и постройки игрока не получают урон от '
                     'противников).',
    'IseeDeadPeople': 'Раскрывает всю карту (очищает от «тумана войны»)',
    'WarpTen': 'Ускоряет подготовку юнитов и постройку строений.',
    'KeyserSoze [количество]': '[количество) ед. золота.',
    'LeafitToMe [количество]': '+ [количество) ед. древесины.',
    'GreedIsGood [количество]': '+ [количество) ед. золота и древесины.',
    'PointBreak': 'Снимает ограничение по числу юнитов.',
    'ThereIsNoSpoon': 'Бесконечная мана для юнитов-магов и героев.',
    'StrengthAndHonor': 'Игра без поражения',
    'Motherland [paca]': 'Переход на указанную миссию в кампании.',
    'SomebodySetUpUsTheBomb': 'Мгновенное поражение',
    'AllYourBaseAreBelongToUs': 'Мгновенная победа',
    'WhoIsJohnGalt': 'Ускоряет прогресс исследований (улучшений)',
    'SharpAndShiny': 'Получение всех улучшений',
    'Synergy': 'Игнорирует древо технологий',
    'RiseAnd Shine': 'Устанавливает время суток день.',
    'LightsOut': 'Устанавливает время суток ночь',
    'DayLightSavings [время]': 'Устанавливает конкретное время суток.',
    'TheDudeAbides': 'Сбрасывает время между атаками юнитов («кулдауны»)',
    'TenthLevelTaurenChieftain': 'Проигрывает песню Power of the horde',
    '=': 'Повторение последней команды',
}
maps = [
    {
        'title': 'Кампания ночных эльфов',
        'subtitle': 'Ужас глубин',
        'missions': [
            {
                'type': 'Ролик',
                'title': 'Пробуждение'
            },
            {
                'type': 'Глава первая',
                'title': 'Наги',
                'map': r'maps\nightElfFT\1\NightElfX01.w3x',
                'map_img': r'maps\nightElfFT\1\map.bmp',
                'description': 'Пылающий Легион больше не угрожает миру, но зло, которое он принес с собой, '
                               'по-прежнему таится в чащобах Ашенвальского леса. Пока друиды и Стражи очищают свой '
                               'край от демонической скверны, Мэв из клана Смотрящих в Ночь, бывшая тюремщица '
                               'Иллидана, идет по следу своего беглого узника, чтобы вновь заковать его в цепи...',
                'img': r'maps\nightElfFT\1\intro.bmp',
            },
            {
                'type': 'Глава вторая',
                'title': 'Таинственные острова',
                'map': r'maps\nightElfFT\2\NightElfX02.w3x',
                'map_img': r'maps\nightElfFT\2\map.bmp',
                'description': 'Прошла ночь. Мэв и ее спутницы высадились на таинственных островах и с удивлением '
                               'обнаружили там древние, но странно знакомые руины...',
                'img': r'maps\nightElfFT\2\intro.bmp',
            }
        ],
    }
]
locate_data = [
    # Восточные Королевства (Eastern Kingdoms)
    {
        "name": "Восточные Королевства",
        "description": "Континент, населенный людьми, дворфами и эльфами. Сильно пострадал от Плети.",
        "main_locate": None
    },
    {
        "name": "Лордерон",
        "description": "Крупное королевство людей, уничтоженное Плетью.",
        "main_locate": "Восточные Королевства"
    },
    {
        "name": "Стратхольм",
        "description": "Город в Лордероне, очищенный принцем Артасом от зараженных жителей.",
        "main_locate": "Лордерон"
    },
    {
        "name": "Андорал",
        "description": "Город в Лордероне, где распространялась чума Плети.",
        "main_locate": "Лордерон"
    },
    {
        "name": "Кель'Талас",
        "description": "Родина Высших Эльфов, уничтоженная Артасом.",
        "main_locate": "Восточные Королевства"
    },
    {
        "name": "Сильвермун",
        "description": "Столица Высших Эльфов в Кель'Таласе.",
        "main_locate": "Кель'Талас"
    },
    {
        "name": "Даларан",
        "description": "Город магов, уничтоженный Архимондом, позже восстановленный.",
        "main_locate": "Восточные Королевства"
    },
    {
        "name": "Серебряный бор",
        "description": "Лес, граничащий с Лордероном, позже зараженный Плетью.",
        "main_locate": "Лордерон"
    },
    {
        "name": "Альтеракские горы",
        "description": "Горный регион, ранее населенный людьми Альтерака, а затем бандитами и ограми.",
        "main_locate": "Восточные Королевства"
    },

    # Нортренд (Northrend)
    {
        "name": "Нортренд",
        "description": "Замороженный континент на севере, место обитания Короля-лича.",
        "main_locate": None
    },
    {
        "name": "Ледяной Трон",
        "description": "Цитадель Короля-лича в Нортренде.",
        "main_locate": "Нортренд"
    },
    {
        "name": "Драконий Погост",
        "description": "Загадочное место в Нортренде, обитель драконов.",
        "main_locate": "Нортренд"
    },

    # Калимдор (Kalimdor)
    {
        "name": "Калимдор",
        "description": "Западный континент, родина орков, ночных эльфов и тауренов.",
        "main_locate": None
    },
    {
        "name": "Оргриммар",
        "description": "Столица орков в Дуротаре, основанная Траллом.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Дуротар",
        "description": "Суровый пустынный регион, родина орков.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Ясеневый лес",
        "description": "Зеленый лес и родина ночных эльфов.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Гора Хиджал",
        "description": "Место финальной битвы с Архимондом.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Степи",
        "description": "Обширная засушливая зона в центре Калимдора, поле сражений.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Оскверненный лес",
        "description": "Проклятый лес, зараженный демоническим влиянием.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Азшара",
        "description": "Мистический регион на восточном побережье Калимдора.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Темные берега",
        "description": "Прибрежная область, обитель ночных эльфов.",
        "main_locate": "Калимдор"
    },
    {
        "name": "Терамор",
        "description": "Человеческий порт, основанный Джайной Праудмур.",
        "main_locate": "Калимдор"
    },

    # Пылающий Легион и Разрушенные Земли
    {
        "name": "Разрушенные Земли",
        "description": "Место вторжения Пылающего Легиона, где находится Темный Портал.",
        "main_locate": "Восточные Королевства"
    },
    {
        "name": "Мир демонов",
        "description": "Родина Пылающего Легиона, населена демонами.",
        "main_locate": None
    },
    {
        "name": "Изумрудный Сон",
        "description": "Мистическая параллельная реальность, связанная с природой Азерота.",
        "main_locate": None
    }
]

item_data = [
    {
        "data": {
            'health': 75,
            'cooldown': 0,
            'mana_cost': 0,
            'damage': 0,
            'duration': 0,
            'coverage_area': 0,
            'casting_range': 0,
            'number_of_targets': 1,
            'damage_per_second': 0,
            'mana_cost_per_second': 0,
            'gold_cost': 175,
            'wood_cost': 0,
            'recharge_interval': 120,  # интервал пополнения
            'start_recharge_interval': 0,  # интервал начального пополнения
            'level': 2,
            'max_quantity': 1,
            'can_be_thrown': True,
            'can_be_purchased_in_shops': True,
            'can_be_sold': True,
            'must_be_activated': False,
            'can_be_depleted': False , # может закончиться
            },
        # 'model': 'default',  # TODO
        'description':'Повышение ловкости, силы и разума героя на 2 ед.',
        'abilities':[], #TODO
        'classification':CLASSES[0][0],
        'name':'Венец благородства',
        'type':TYPES[0][0],
        'autocast':False,
        'image':'', #TODO
        'video':'',
        'hotkey':'C',
        'hotkey_ru':'С',
        'audio':'',
    }
]



def get_target(target,get_id=True):
    get_tar = Targets.objects.get(name_ru=target)
    if get_id:
        return get_tar.id
    return get_tar
upgrade_data = [
    {
        'names': ["Железные мечи", "Стальные мечи", "Мифрильные мечи"],
        'description': 'Увеличение урона, наносимого ополченцами, пехотинцами, ведьмаками, ястребами, рыцарями и грифонами в ближнем бою.',
        'effects': {
            'Дополнительная атака(кости)': 1,
        },
        'wood_cost': '50',
        'gold_cost': '100',
        'images':  [],  # TODO
        'hotkey': 'S',
        'hotkey_ru': 'Ы',
        'wood_cost_level': '125',
        'gold_cost_level': '75',
        'time_cost': '60',
        'time_cost_level': '15',
        'needed_technologies': {
            '1': [],
            '2': [],  # TODO
            '3': [],
        },
    }
]




def calc(char):
    # formulas
    # char['data']['attack_diapason'] = (char['data']['dice'] - 1) * char['data']['sides']
    # char['data']['attack_diapason_2'] = (char['data']['dice_2'] - 1) * char['data']['sides_2']
    # char['data']['attack_damage_min'] = char['data']['damage'] + char['data']['dice']
    # char['data']['attack_damage_max'] = char['data']['attack_damage_min'] + char['data']['attack_diapason']
    # char['data']['attack_damage_min_2'] = char['data']['damage_2'] + char['data']['dice_2']
    # char['data']['attack_damage_max_2'] = char['data']['attack_damage_min_2'] + char['data']['attack_diapason_2']
    return char


def data_loader():
    for target in targets:
        Targets.objects.get_or_create(name_ru=target[1], name_en=target[0])

    char_data = [
            {
                'data': {
                    'health': 220,
                    'mana': 0,
                    'build_time': 15,
                    'health_regeneration': 0.25,
                    'mana_regeneration': 0,
                    'gold_cost': 75,
                    'wood_cost': 0,
                    'food_cost': 1,
                    'sight_range_day': 800,
                    'sight_range_night': 600,
                    'attack_speed': 2,
                    'repair_time': 15,
                    'repair_gold_cost': 75,
                    'repair_wood_cost': 0,
                    'attack_area': 0,
                    'damage': 4,
                    'movement_speed': 190,
                    'attack_range': 90,
                    'defence': 0,
                    'types_of_attack': types_of_attack[1][0],
                    'attack_targets': [get_target(targets[8][1]), get_target(targets[10][1]),
                                       get_target(targets[14][1]),
                                       get_target(targets[23][1]), get_target(targets[24][1])],
                    'attack_speed_2': 1.1,
                    'attack_area_2': 0,
                    'damage_2': 0,
                    'attack_range_2': 66,
                    'attack_targets_2': [get_target(targets[5][1])],
                    'types_of_attack_2': types_of_attack[1][0],
                    'attacks': 2,
                    'sides': 1,
                    'dice': 2,
                    'sides_2': 1,
                    'dice_2': 1,
                    'add_defence': 2,
                    'level': 1,
                },
                'health_regeneration_time': health_regeneration_types[1][0],
                'name': 'Работник',
                'race': races[0][0],
                'description': 'Мастер на все руки. Может добывать золото и рубить лес, а также строить новые здания и '
                               'ремонтировать поврежденные. При необходимости способен взяться за оружие, записавшись в '
                               'ополчение.',
                'tip': 'Может атаковать наземные цели',
                'movement_type': movement_types[1][0],
                'image_name':'peasant.jpg',
                'type_of_defence': types_of_defence[2][0],
                'is_build': False,
                'can_build': True,
                'can_train': False,
                'hotkey': 'P',
                'hotkey_ru': 'З',
                'type_unit': [get_target(targets[14][1]),],
                'chars_builds': [],  # TODO
                'skills': [],  # TODO
                'model': None,  # TODO
                'upgrades': []  # TODO,
            },
        ]
    char_data[0]['image'] = get_file(name=char_data[0]['image_name'], char_name=char_data[0]['name'], folder=os.path.join(images_dir, 'chars')),
    print(char_data[0]['image'])
    hero_data = [
            {
                'data': {
                    'health': 100,
                    'mana': 200,
                    'health_regeneration': 0.25,
                    'mana_regeneration': 0.01,
                    'build_time': 55,
                    'repair_time': 55,
                    'gold_cost': 425,
                    'wood_cost': 100,
                    'repair_gold_cost': 425,
                    'repair_wood_cost': 100,
                    'food_cost': 0,
                    'sight_range_day': 1800,
                    'sight_range_night': 800,
                    'attack_speed': 2.2,
                    'attack_area': 0,
                    'damage': 0,
                    'attack_range': 100,
                    'movement_speed': 270,
                    'defence': 2,
                    'types_of_attack': types_of_attack[7][0],
                    'attack_targets': [get_target(targets[8][1]), get_target(targets[10][1]),
                                       get_target(targets[14][1]),
                                       get_target(targets[23][1]), get_target(targets[24][1])],
                    'attack_speed_2': 2.13,
                    'attack_area_2': 0,
                    'damage_2': 0,
                    'attack_range_2': 500,
                    'attack_targets_2': [get_target(targets[8][1]), get_target(targets[10][1]),
                                         get_target(targets[14][1]),
                                         get_target(targets[23][1]), get_target(targets[24][1]),
                                         get_target(targets[0][1])],
                    'types_of_attack_2': types_of_attack[2][0],
                    'attacks': 1,
                    'sides': 6,
                    'dice': 2,
                    'sides_2': 4,
                    'dice_2': 2,
                    'add_defence': 0,
                    'level': 1,

                    'intelligence': 17,
                    'agility': 13,
                    'strength': 22,
                    'agility_per_level': 1.5,
                    'strength_per_level': 2.7,
                    'intelligence_per_level': 1.8,
                    'max_level': 10,
                },
                'type_unit': [get_target(targets[14][1]), ],
                'primary_attribute': primary_attributes[0],
                'health_regeneration_time': health_regeneration_types[1][0],
                'name': 'Артес',
                'second_name': 'Паладин',
                'race': races[0][0],
                'description': "Герой-воин, в совершенстве владеющий искусством обороны. Находясь рядом с ним, дружественные "
                               "войска сражаются эффективнее. Способен выучить заклинания ''Благодать'', ''Божественный "
                               "щит'', ''Доспехи веры'' и ''Воскрешение'.",
                'tip': 'Может атаковать наземные цели.',
                'movement_type': movement_types[1][0],
                'type_of_defence': types_of_defence[5][0],
                'is_build': False,
                'can_build': False,
                'can_train': False,
                'hotkey': 'L',
                'hotkey_ru': 'Д',
                'image_name': 'arthasPaladin.jpg',


                'model': None,  # TODO
                'skills': [],  # TODO
            },
        ]
    hero_data[0]['image'] = get_file(name=hero_data[0]['image_name'], char_name=hero_data[0]['name'], folder=os.path.join(images_dir, 'heroes')),
    Constants.objects.get_or_create()

    sounds_units_arthas_replics_dir = os.path.join(current_dir, 'sounds', 'units', 'arthas', 'replics')
    sounds_units_arthas_ability_sounds_dir = os.path.join(current_dir, 'sounds', 'units', 'arthas', 'ability_sounds')
    sounds_musics_dir = os.path.join(current_dir, 'sounds', 'musics')


    for video in videos:
        folder = os.path.join(current_dir, videos[video])
        with open(folder, 'rb') as file:
            django_file = File(file, name=videos[video])
            Video.objects.get_or_create(description=video, video=django_file, category='game_video',
                                        name='Видео из игры')

    for video in game_videos:
        folder = os.path.join(current_dir, game_videos[video])
        with open(folder, 'rb') as file:
            django_file = File(file, name=game_videos[video])
            Video.objects.get_or_create(description=video, video=django_file, category='game_process')

    import_files_from_folder(model=Image, folder_path=images_dir, name='image')
    import_files_from_folder(model=Audio, folder_path=sounds_units_arthas_replics_dir, name='audio',
                             main_data={'category': 'Replays'})
    import_files_from_folder(model=Audio, folder_path=sounds_units_arthas_ability_sounds_dir, name='audio',
                             main_data={'category': 'Ability_Sound'})
    import_files_from_folder(model=Audio, folder_path=sounds_musics_dir, name='audio', main_data={'category': 'Music'})

    Cheats.objects.get_or_create(data=cheats)

    for map_ in maps:
        for mission in map_['missions']:
            if mission['type'] == 'Ролик':
                Maps.objects.get_or_create(
                    campaign_title=map_['title'],
                    campaign_subtitle=map_['subtitle'],
                    title=mission['title'],
                    type=mission['type'],
                )
                continue

            folder_map_img = os.path.join(current_dir, mission['map_img'])
            folder_img = os.path.join(current_dir, mission['img'])
            folder_file = os.path.join(current_dir, mission['map'])

            with open(folder_map_img, 'rb') as file:
                django_file_map_img = File(file, name=mission['map_img'])
                img_1, created_img1 = Image.objects.get_or_create(image=django_file_map_img, name='map_img')

            with open(folder_img, 'rb') as file:
                django_file_img = File(file, name=mission['img'])
                img_2, created_img2 = Image.objects.get_or_create(image=django_file_img, name='img')

            with open(folder_file, 'rb') as file:
                django_file_main = File(file, name=mission['map'])

                map_obj, created_map = Maps.objects.get_or_create(
                    campaign_title=map_['title'],
                    campaign_subtitle=map_['subtitle'],
                    type=mission['type'],
                    title=mission['title'],
                    file=django_file_main,
                    description=mission['description']
                )

                map_obj.images.add(img_1)
                map_obj.images.add(img_2)
                map_obj.save()

    for locate in locate_data:
        locate_obj, created = Locate.objects.get_or_create(
            name=locate['name'],
            description=locate['description'],
        )

        if locate['main_locate']:
            main_locate_obj = Locate.objects.get(name=locate['main_locate'])
            locate_obj.main_locate = main_locate_obj
            locate_obj.save()

    for upgrade in upgrade_data:
        levels = len(upgrade['names'])
        print(levels)
        Upgrade.objects.get_or_create(
            levels=levels,
            names=upgrade['names'],
            description=upgrade['description'],
            effects=upgrade['effects'],
            wood_cost=upgrade['wood_cost'],
            gold_cost=upgrade['gold_cost'],
            wood_cost_level=upgrade['wood_cost_level'],
            gold_cost_level=upgrade['gold_cost_level'],
            time_cost=upgrade['time_cost'],
            time_cost_level=upgrade['time_cost_level'],
            hotkey=upgrade['hotkey'],
            hotkey_ru=upgrade['hotkey_ru'],
            needed_technologies=upgrade['needed_technologies'],
        )

    for char in char_data:
        char = calc(char)
        char_obj, created = CharacterOrBuild.objects.get_or_create(
            data=char['data'],
            health_regeneration_time=char['health_regeneration_time'],
            name=char['name'],
            race=char['race'],
            description=char['description'],
            tip=char['tip'],
            movement_type=char['movement_type'],
            type_of_defence=char['type_of_defence'],
            is_build=char['is_build'],
            can_build=char['can_build'],
            can_train=char['can_train'],
            hotkey=char['hotkey'],
            hotkey_ru=char['hotkey_ru'],
            image=char['image'][0],

        )

        type_unit_data = char.get('type_unit', [])
        if type_unit_data:
            for type_unit in type_unit_data:
                char_obj.type_unit.add(type_unit)
        char_obj.save()

    for char in hero_data:
        char = calc(char)
        # formulas char['data']['health'] = char['data']['health'] + char['data']['strength'] *
        # constants.str_bonus_health char['data']['health_regeneration'] = char['data']['health'] + char['data'][
        # 'strength'] * constants.str_bonus_heal

        # char['data']['mana'] = char['data']['health'] + char['data']['strength'] * constants.int_bonus_mana char[
        # 'data']['mana_regeneration'] = char['data']['health'] + char['data']['strength'] *
        # constants.int_bonus_mana_regen

        # char['data']['defence'] = char['data']['defence'] + char['data']['agility'] * constants.agi_bonus_def char[
        # 'data']['attack_speed'] = char['data']['attack_speed'] - char['data']['agility'] *
        # constants.agi_bonus_attack_speed char['data']['attack_speed_2'] = char['data']['attack_speed_2'] - char[
        # 'data']['agility'] * constants.agi_bonus_attack_speed

        # char['data']['gold_cost'] = char['data']['gold_cost'] * constants.hero_gold_cost + char['data'][
        # 'gold_cost'] * (char['data']['level'] - 1) * constants.hero_gold_cost_level char['data']['wood_cost'] =
        # char['data']['wood_cost'] * constants.hero_wood_cost + char['data']['wood_cost'] * (char['data']['level'] -
        # 1) * constants.hero_wood_cost_level char['data']['gold_cost_moment'] = (char['data']['gold_cost'] *
        # constants.hero_gold_cost_moment + char['data']['gold_cost'] * (char['data']['level'] - 1) *
        # constants.hero_gold_cost_level) char['data']['wood_cost_moment'] = (char['data']['wood_cost'] *
        # constants.hero_wood_cost_moment + char['data']['wood_cost'] * (char['data']['level'] - 1) *
        # constants.hero_wood_cost_level)

        # char['data']['defence'] = char['data']['defence'] + constants.start_def

        # time = char['data']['build_time'] * char['data']['level'] * constants.hero_time_cost
        # max_time = char['data']['build_time']  * constants.hero_time_cost_max
        # if time > max_time:
        #     char['data']['build_time'] = max_time
        #     char['data']['repair_time'] = max_time
        # else:
        #     char['data']['build_time'] = time
        #     char['data']['repair_time'] = time

        hero_obj, created = Hero.objects.get_or_create(
            data=char['data'],
            # model=char['model'],
            name=char['name'],
            second_name=char['second_name'],
            race=char['race'],
            description=char['description'],
            tip=char['tip'],
            movement_type=char['movement_type'],
            image=char['image'][0],
            type_of_defence=char['type_of_defence'],
            is_build=char['is_build'],
            can_build=char['can_build'],
            can_train=char['can_train'],
            health_regeneration_time=char['health_regeneration_time'],
            hotkey=char['hotkey'],
            hotkey_ru=char['hotkey_ru'],
            primary_attribute=char['primary_attribute'],
            is_hero=True
        )
        type_unit_data = char.get('type_unit', [])
        if type_unit_data:
            hero_obj.type_unit.set(type_unit_data)
        hero_obj.save()


    for item in item_data:
        Item.objects.get_or_create(
            data=item['data'],
            name=item['name'],
            description=item['description'],
            classification=item['classification'],
            type=item['type'],
            autocast=item['autocast'],
            # image=item['image'],
            # video=item['video'],
            hotkey=item['hotkey'],
            hotkey_ru=item['hotkey_ru'],
            # audio=item['audio'],
        )

    # for key, value in attributes_data.items():
    #     Attribute.objects.create(name=key, icon=value)
