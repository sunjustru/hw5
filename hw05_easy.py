import os


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def do_folder(action, folder):
    if action == 'make':
        os.mkdir(folder)
    else:
        os.rmdir(folder)


# do_folder('make', 'dir_1')
# do_folder('del', 'dir_1')

files = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
# Создание директорий
[do_folder('make', itm) for itm in files]
# Удаление директорий
[do_folder('del', itm) for itm in files]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
