import os
import shutil
__file__ = 'hw05_easy.py'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def folder_make(folder):
    folder = os.path.join(os.getcwd(), folder)
    try:
        os.mkdir(folder)
        print("Вы создали папку — " + folder)
    except:
        print("Не получается создать папку, она уже существует!")


def folder_del(folder):
    folder = os.path.join(os.getcwd(), folder)
    try:
        os.rmdir(folder)
        print("Вы удалили папку — " + folder)
    except:
        print("Не получается удалить папку, она не существует")

[folder_make('dir_' + str(itm)) for itm in range(1,10)]
[folder_del('dir_' + str(itm)) for itm in range(1,10)]
# def do_folder(action, folder):
#     if action == 'make':
#         os.mkdir(folder)
#     else:
#         os.rmdir(folder)
#
#
# files = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
# # # Создание директорий
# [do_folder('make', itm) for itm in files] # rage(1,10) — можно;
# # # Удаление директорий
# [do_folder('del', itm) for itm in files]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_folder(folder):
    def file_or_folder(name):
        if os.path.isfile(name):
            return 'файл — ' + name
        else:
            return 'папка — ' + name + '/'

    print("\n".join([file_or_folder(itm) for itm in os.listdir(folder)]))

show_folder(os.getcwd())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(file_1, file_2):
    if not file_1:
        print('Укажите название копируемого файла')
        return
    if not file_2:
        print('Укажите название копируемого как назвать файл')
        return
    shutil.copy2(file_1, file_2)

copy_file(__file__, __file__ + '_copy')