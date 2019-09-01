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
# https://www.youtube.com/watch?v=jiZM2p99XO4&feature=youtu.be Типо как работает

import os
from hw05_easy import *

# def show_folder(folder):
#     def file_or_folder(name):
#         if os.path.isfile(name):
#             return 'файл — ' + name
#         else:
#             return 'папка — ' + name + '/'
#
#     print("\n".join([file_or_folder(itm) for itm in os.listdir(folder)]))


# def folder_make(folder):
#     try:
#         os.mkdir(console_utility_dir + '/' + folder)
#         print("Вы создали папку — " + console_utility_dir + '/' + folder)
#     except:
#         print("Не получается создать папку, она уже существует!")
#
#
# def folder_del(folder):
#     try:
#         os.rmdir(console_utility_dir + '/' + folder)
#         print("Вы удалили папку — " + console_utility_dir + '/' + folder)
#     except:
#         print("Не получается удалить папку, она не существует")


console_utility = {
    'do': {
        '1': {
            'name': ['Перейти в папку: ', '## Укажите название папки: '],
            'fn': None,
            'f_name': None  # Указываем название сущности (название папки)
        },
        '2': {
            'name': ['Просмотреть содержимое текущей папки: '],
            'fn': show_folder,
            'f_name': None  # Указываем название сущности (название папки)
        },
        '3': {
            'name': ['Удалить папку: ', '## Укажите название папки: '],
            'fn': folder_del,
            'f_name': None  # Указываем название сущности (название папки)
        },
        '4': {
            'name': ['Создать папку: ', '## Укажите название папки: '],
            'fn': folder_make,
            'f_name': None  # Указываем название сущности (название папки)
        },
        '5': {
            'name': ['Выйти из программы: '],
            'fn': "Тут будет название функции make_folder",
            'f_name': None  # Указываем название сущности (название папки)
        }
    }
}

# Переменные
console_utility_bool = True
# путь по умолчанию
console_utility_dir = os.path.join(os.getcwd())
console_utility_parent = os.path.join(os.getcwd())

def build_menu():
    menu_text = '################### МЕНЮ \n'
    if console_utility_dir != os.path.abspath('.'):
        menu_text = menu_text + '### [top] — Перейти в главную директорию \n'
        menu_text = menu_text + '### [back] — Вернуться в предыдущую директорию \n'
    for itm in console_utility['do']:
        menu_text = menu_text + '# [' + itm + '] ' + console_utility['do'][itm]['name'][0] + '\n'
    return menu_text + '###################\n'


while console_utility_bool:
    print(build_menu())
    what_do = input('# Выберите пункт меню: ')

    # Ограничиваем хождение по директориям потомка!
    if console_utility_dir != console_utility_parent and what_do == 'back':
        #console_utility_dir = os.path.split(console_utility_dir)[0]
        continue
    elif what_do == 'top':
        console_utility_dir = os.chdir(console_utility_parent)

    if what_do in console_utility['do']:
        # Если клиент хочет выйти из программы
        if int(what_do) == 5:
            console_utility_bool = False
            break

        if int(what_do) == 2:
            temp = os.path.join(os.getcwd())
        else:
            name = console_utility['do'][what_do]['name'][1]
            temp = input(name)

        # Если мы решили перейти в другую папку
        # Делаем проверку на существование папки и сохранить новый путь console_utility_dir
        if int(what_do) == 1:
            if os.path.exists(os.getcwd() + '/' + temp):
                console_utility_dir = os.chdir(os.getcwd() + '/' + temp)
            else:
                print('#### Директории не существует! ####')
        else:
            console_utility['do'][what_do]['fn'](temp)


    else:
        print('### Данного действия нет! ###')

if console_utility_bool == False:
    print('До свидание!')

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
