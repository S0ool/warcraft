import os
from django.core.files.base import File

from wft.models import Image


def get_file(folder, name,char_name):
    img_path = os.path.join(folder, name)
    with open(img_path, 'rb') as file:
        django_file = File(file, name=name)
        img, created = Image.objects.get_or_create(image=django_file, name=char_name)
    cur_img = Image.objects.filter(name=char_name).first()
    return cur_img

def import_files_from_folder(folder_path, model, name, main_data=None):
    if not main_data:
        main_data = {}

    # Проверяем существование папки
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не найдена.")
        return

    # Перебираем файлы в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                # Открываем файл как Django File объект, вне блока 'with'
                with open(file_path, 'rb') as file:
                    django_file = File(file, name=filename)  # Обертываем файл в объект Django File

                    # Создаем копию main_data с файлом
                    data_with_file = main_data.copy()
                    data_with_file[name] = django_file  # Добавляем django_file в data

                    # Сохраняем объект в базе данных
                    print(data_with_file)
                    model.objects.get_or_create(**data_with_file)

                print(f"Файл {filename} обработан и добавлен в БД.")

            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {e}")

