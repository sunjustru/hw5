# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <dir_name> - название файла; <file_name> - новое название файла для копирования")
    print("rm <dir_name> - удаляем указанный файл")
    print("cd <dir_name> - путь новой директории")
    print("ls — выводим полный ключ к текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла который вы хотите скопировать")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        shutil.copy2(dir_name, file_name)
        print('файл {} скопирован'.format(dir_name))
    except FileNotFoundError:
        #TODO: Нет проверки на есть файл с таким названием или нет
        print('файд {} с таким именем уже существует'.format(dir_name))

def rm_file():
    if not dir_name:
        print("Необходимо указать имя файла который вы хотите удалить")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_name)
        print('файл {} удалён'.format(dir_name))
    except FileNotFoundError:
        # TODO: Нет проверки на есть файл с таким названием или нет
        print('файл {} не найден'.format(dir_name))

def ls_dir():
    print('Полный путь к текущей директории: ' +os.path.join(os.getcwd()))

def cd_dir():
    if not dir_name:
        print("Необходимо директорию для перехода")
        return
    try:
        os.chdir(dir_name)
        print('вы перешли в директорию {}'.format(dir_name))
    except FileNotFoundError:
        # TODO: Нет проверки на есть файл с таким названием или нет
        print('директория {} не найдена'.format(dir_name))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp' : copy_file,
    'rm': rm_file,
    'cd': cd_dir,
    'ls': ls_dir
}

try:
    file_name = sys.argv[3]
except IndexError:
    file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")