# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import os
import pprint

def show_folder(folder):
    print(os.listdir(folder))

def folder_cd(folder):
    pass

def folder_make(folder):
    result = False
    try:
        os.mkdir(folder)
        result = True
    except:
        print("Не получается создать папку, она уже существует!")
    return result

def folder_del(folder):
    result = False
    try:
        os.rmdir(folder)
        result = True
    except:
        print("Не получается удалить папку, она не существует")
    return result


console_utility = {
    'do': {
        '1': {
            'name': 'Перейти в папку: ',
            'fn': "Тут будет название функции move_folder",
            'f_name': None  # Указываем название сущности (название папки)
        },
        '2': {
            'name': 'Просмотреть содержимое текущей папки: ',
            'fn': show_folder,
            'f_name': None  # Указываем название сущности (название папки)
        },
        '3': {
            'name': 'Удалить папку: ',
            'fn': folder_del,
            'f_name': None  # Указываем название сущности (название папки)
        },
        '4': {
            'name': 'Создать папку: ',
            'fn': folder_make,
            'f_name': None  # Указываем название сущности (название папки)
        },
        '5': {
            'name': 'Выйти из программы: ',
            'fn': "Тут будет название функции make_folder",
            'f_name': None  # Указываем название сущности (название папки)
        }
    },
    'question': {
        '1': 'Уточните название папки',
        '3': 'Уточните название папки',
        '4': 'Уточните название папки'
    },
    'error': {
        '1': 'Невозможно перейти в папку',
        '3': 'Невозможно удалить папку',
        '4': 'Невозможно создать папку'
    }
}

# Переменные
console_utility_bool = True
console_utility_dir = '.'
console_utility_folder_name = None

def build_menu():
    menu_text = ''
    for itm in console_utility['do']:
        menu_text = menu_text + '[' + str(itm) + '] ' + str(console_utility['do'][itm]['name'] + '\n')
    return menu_text


print(build_menu())

while console_utility_bool:

    what_do = input('Выберите пункт меню: ')

    if what_do in console_utility['do']:
        # Если клиент хочет выйти из программы
        if int(what_do) == 5:
            console_utility_bool = False
            break

        id = what_do
        name = console_utility['do'][what_do]['name']

        temp = input(name)
        console_utility_folder_name = temp

        # Запускаем функцию
        result = console_utility['do'][what_do]['fn'](console_utility_folder_name)

        print(result)


    else:
        print('Данного действия нет!')
        print(build_menu())

if console_utility_bool == False:
    print('До свидание!')

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
