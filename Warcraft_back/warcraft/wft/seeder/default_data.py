from django.core.files.base import File
from .load_from_dir import import_files_from_folder
from ..models import *
import os

#TODO добавить все данные, распределить по файлам и проверить корректность
targets = [
    ('Airborne', 'Воздушные'),
    ('PlayerUnits', 'Войска игрока'),
    ('Enemies', 'Враги'),
    ('Heroes', 'Герои'),
    ('Decorations', 'Декорации'),
    ('Woods', 'Деревья'),
    ('Trees', 'Древа'),
    ('Friends', 'Друзья'),
    ('Spirits', 'Духи'),
    ('Living', 'Живые'),
    ('Buildings', 'Здания'),
    ('Dead', 'Мертвые'),
    ('Mechanisms', 'Механизмы'),
    ('Bridges', 'Мосты'),
    ('Ground', 'Наземные'),
    ('NotTrees', 'Не древа'),
    ('NotHeroes', 'Не герои'),
    ('NotWarrior', 'Не сам воин'),
    ('NotSuicidal', 'Не самоубийцы'),
    ('Neutral', 'Нейтральные'),
    ('None', 'Нет'),
    ('Invulnerable', 'Неуязвимые'),
    ('Organisms', 'Организмы'),
    ('Items', 'Предметы'),
    ('Others', 'Прочее'),
    ('Relief', 'Рельеф'),
    ('Warrior', 'Сам воин'),
    ('Suicidal', 'Самоубийцы'),
    ('Allies', 'Союзники'),
    ('Walls', 'Стены'),
    ('Vulnerable', 'Уязвимые')
]
videos = {
    'Исход Орды: Пророчество': 'videos\TutorialIn.mp4',
    'Исход Орды: Сон Тралла': 'videos\TutorialOp.mp4',
    'Падение Лордерона: Предупреждение': 'videos\HumanOp.mp4',
    'Падение Лордерона: Предательство Артеса': 'videos\HumanEd.mp4',
    'Путь Проклятых: Разрушение Даларана': r'videos\UndeadEd.mp4',
    'Вторжение на Калимдор: Гибель Задиры': r'videos\OrcEd.mp4',
    'Конец Вечности': r'videos\NightElfEd.mp4',
    'Ужас из Глубин - Пробуждение': 'videos\IntroX.mp4',
    'Повелитель Тьмы - Финал Время настало': r'videos\Arthas_vs_Ilidan.mp4',
    'Повелитель Тьмы - Ролик: Восхождение': r'videos\OutroX.mp4',
}
game_videos = {
    'Как установить и запустить Warcraft 3 на Windows 10?': r'videos\game_process\download.mp4',
    '⚡ Warcraft 3 Frozen Throne⚡Часть 1⚡Кампания Ночных Эльфов⚡Глава первая⚡Наги⚡': r'videos\game_process\part_1.mp4',
}
cheats = {
    'WhosYourDaddy':'Запуск «Режима Бога» (убийства с одного удара, юниты и постройки игрока не получают урон от противников).',
    'IseeDeadPeople':'Раскрывает всю карту (очищает от «тумана войны»)',
    'WarpTen':'Ускоряет подготовку юнитов и постройку строений.',
    'KeyserSoze [количество]':'[количество) ед. золота.',
    'LeafitToMe [количество]':'+ [количество) ед. древесины.',
    'GreedIsGood [количество]':'+ [количество) ед. золота и древесины.',
    'PointBreak':'Снимает ограничение по числу юнитов.',
    'ThereIsNoSpoon':'Бесконечная мана для юнитов-магов и героев.',
    'StrengthAndHonor':'Игра без поражения',
    'Motherland [paca]':'Переход на указанную миссию в кампании.',
    'SomebodySetUpUsTheBomb':'Мгновенное поражение',
    'AllYourBaseAreBelongToUs':'Мгновенная победа',
    'WhoIsJohnGalt':'Ускоряет прогресс исследований (улучшений)',
    'SharpAndShiny':'Получение всех улучшений',
    'Synergy':'Игнорирует древо технологий',
    'RiseAnd Shine':'Устанавливает время суток день.',
    'LightsOut':'Устанавливает время суток ночь',
    'DayLightSavings [время]':'Устанавливает конкретное время суток.',
    'TheDudeAbides':'Сбрасывает время между атаками юнитов («кулдауны»)',
    'TenthLevelTaurenChieftain':'Проигрывает песню Power of the horde',
    '=':'Повторение последней команды',
}
maps = [
    {
        'title':'Кампания ночных эльфов',
        'subtitle':'Ужас глубин',
        'missions':[
            {
                'type':'Ролик',
                'title':'Пробуждение'
            },
            {
                'type':'Глава первая',
                'title':'Наги',
                'map':r'maps\nightElfFT\1\NightElfX01.w3x',
                'map_img':r'maps\nightElfFT\1\map.bmp',
                'description':'Пылающий Легион больше не угрожает миру, но зло, которое он принес с собой, по-прежнему таится в чащобах Ашенвальского леса. Пока друиды и Стражи очищают свой край от демонической скверны, Мэв из клана Смотрящих в Ночь, бывшая тюремщица Иллидана, идет по следу своего беглого узника, чтобы вновь заковать его в цепи...',
                'img':r'maps\nightElfFT\1\intro.bmp',
            },
            {
                'type':'Глава вторая',
                'title':'Таинственные острова',
                'map':r'maps\nightElfFT\2\NightElfX02.w3x',
                'map_img':r'maps\nightElfFT\2\map.bmp',
                'description':'Прошла ночь. Мэв и ее спутницы высадились на таинственных островах и с удивлением обнаружили там древние, но странно знакомые руины...',
                'img':r'maps\nightElfFT\2\intro.bmp',
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



# images = [
#     'images\first.avif',
#     'images\second.avif',
#     'images\third.avif',
#     'images\fourth.webp',
#     'images\fifth.jpg',
#     'images\sixth.jpg',
#     'images\seventh.jpg',
#     'images\eighth.jpg',
#     'images\ninth.jpg',
#     'images\tenth.jpg',
#     'images\eleventh.jpg',
#     'images\twelfth.jpg',
#     'images\thirteenth.jpg',
#     'images\fourteenth.png',
#     'images\fifteenth.jpg',
#
# ]
Char_or_build_data = [
    {
        'data':{
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
    'defence':0,},
        'name':'name',
        'race':'Alliance',
        'description':'description',
        'movement_type':'Pedestrian',
        'image': 'image',

    },
]



def data_loader():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    images_dir = os.path.join(current_dir, 'images')
    sounds_units_arthas_replics_dir = os.path.join(current_dir, 'sounds', 'units', 'arthas', 'replics')
    sounds_units_arthas_ability_sounds_dir = os.path.join(current_dir, 'sounds', 'units', 'arthas', 'ability_sounds')
    sounds_musics_dir = os.path.join(current_dir, 'sounds', 'musics')

    for target in targets:
        Targets.objects.get_or_create(name_ru=target[0], name_en=target[1])

    for video in videos:
        folder = os.path.join(current_dir, videos[video])
        with open(folder, 'rb') as file:
            django_file = File(file,name=videos[video])
            Video.objects.get_or_create(description=video, video=django_file, category='game_video', name='Видео из игры')

    for video in game_videos:
        folder = os.path.join(current_dir, game_videos[video])
        with open(folder, 'rb') as file:
            django_file = File(file, name=game_videos[video])
            Video.objects.get_or_create(description=video, video=django_file,  category='game_process')

    import_files_from_folder(model=Image, folder_path=images_dir, name='image')
    import_files_from_folder(model=Audio, folder_path=sounds_units_arthas_replics_dir, name='audio',
                             main_data={'category': 'Replays'})
    import_files_from_folder(model=Audio, folder_path=sounds_units_arthas_ability_sounds_dir, name='audio',
                             main_data={'category': 'Ability_Sound'})
    import_files_from_folder(model=Audio, folder_path=sounds_musics_dir, name='audio', main_data={'category': 'Music'})

    Cheats.objects.get_or_create(data=cheats)

    for map in maps:
        for mission in map['missions']:
            if mission['type'] == 'Ролик':
                Maps.objects.get_or_create(
                    campaign_title=map['title'],
                    campaign_subtitle=map['subtitle'],
                    title=mission['title'],
                    type=mission['type'],
                )
                continue

            # Определяем пути к файлам
            folder_map_img = os.path.join(current_dir, mission['map_img'])
            folder_img = os.path.join(current_dir, mission['img'])
            folder_file = os.path.join(current_dir, mission['map'])

            # Открываем и создаем или получаем объекты изображений
            with open(folder_map_img, 'rb') as file:
                django_file_map_img = File(file, name=mission['map_img'])
                img_1, created_img1 = Image.objects.get_or_create(image=django_file_map_img, name='map_img')

            with open(folder_img, 'rb') as file:
                django_file_img = File(file, name=mission['img'])
                img_2, created_img2 = Image.objects.get_or_create(image=django_file_img, name='img')

            # Открываем основной файл
            with open(folder_file, 'rb') as file:
                django_file_main = File(file, name=mission['map'])

                # Создаем или получаем объект карты
                map_obj, created_map = Maps.objects.get_or_create(
                    campaign_title=map['title'],
                    campaign_subtitle=map['subtitle'],
                    type=mission['type'],
                    title=mission['title'],
                    file=django_file_main,
                    description=mission['description']
                )

                # Добавляем изображения к ManyToMany полю и сохраняем
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


    # for image in images:
    #     Image.objects.create(image=image)





    # for key, value in attributes_data.items():
    #     Attribute.objects.create(name=key, icon=value)
