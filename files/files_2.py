# закрытие файла
hosts = open('data.txt') #открываем файл
hosts_file_contents = hosts.read() # читаем файл
print(hosts_file_contents)
hosts.close() # закрываем файл

# проверка закрыт ли файл
hosts = open('data.txt')
hosts_file_contents = hosts.read()
print('File closed? {}'.format(hosts.closed))
if not hosts.closed:
    hosts.close()

print('File closed? {}'.format(hosts.closed))

# Автоматическое закрытие файла при помощи with
print('Started reading the file.')
with open('data.txt') as hosts:
    print('File closed? {}'.format(hosts.closed))
    print(hosts.read())
print('Finished reading the file.')
print('File closed? {}'.format(hosts.closed))

# Использование циклов в файлах
with open('data.txt') as data:
    for line in data:
        print(line)

# режимы открытия файла
# open(path_to_file, mode)
# r - open for reading(default) === открыт для чтения (по умолчанию)
# w - open for writing, truncating first === открыт для записи, сначала укороченный
# x - Create a new file and open it for writing === Создать новый файл и открыть его для записи
# a - open for writing, appending to file === открыть для записи, добавив в уже записанный файл
# + - open a file for updating (read/write) === открыть файл для обновления (чтение / запись)
# b - Binary mode === Бинарный режим
# t - Text mode (default) === Текстовый режим (по умолчанию)

# Открытие и запись новых данных в файл
with open('data.txt', 'w') as data:
    data.write('This text will be written to the file.')
    data.write('Here is more text.')

with open('data.txt') as data:
    print(data.read())

# Carriage returns and line feeds === Возврат каретки и перевод строки
# \r - Carriage return === Возврат каретки
# \n - new line === новая строка
# \n - Unix/Linux/Mac line endings. === Unix/Linux/Mac конец сроки
# \r\n - Windows style line endings ===  Windows конец сроки

# Открытие и запись новых данных в файл, используя символ перевода строки в конце строки
with open('data.txt', 'w') as data:
    data.write('This text will be written to the file. \n')
    data.write('Here is more text. \n')

with open('data.txt') as data:
    print(data.read())

# Binary files работа с бинарными файлами
with open('C:\Users\andrey.kutenev\Downloads\1207_2019-07-10_PLN_01_00.jpg', 'rb') as picture:
    picture.seek(2)
    picture.read(4)
    print(picture.tell())
    print(picture.mode)

# Исключения при работе с файлами
# Open a file and assign its contents to variable.
# If the  file is unavailable, create an empty variable.

try:
    contacts = open('contacts.txt').read()
except:
    contacts = ''

print(len(contacts))
