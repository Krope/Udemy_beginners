# Открытие файлов
#open('C:\Users\andrey.kutenev\Downloads\image-01-04-20-05-59-1.heic')

# Чтение файлов
hosts = open('data.txt')
hosts_file_contents = hosts.read()
print(hosts_file_contents)

#read() - Returns the entire file(Возвращает весь файл)
#seek(offset) - Change the current position to offset(Изменить текущую позицию на смещение)
#seek(0) - go to the beginning of the file(перейти к началу файла)
#seek(5) - go to the 5th byte of the file(перейти к 5-му байту файла)
#tell() - determine the current position in the file(определить текущую позицию в файле)

# Current position: 0 начали чтение с нуля, поэтому позиция 0
hosts = open('data.txt')
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())
# Current position: 110 после прочтения файла кончная позиция
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())
# Current position: 0 вернулись в начало файла
hosts.seek(0)
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())

# Чтение файла с заданной позиции
hosts = open('data.txt')
print(hosts.read(3)) # задаем позицию с которой начинаем чтение файла
print(hosts.tell())
