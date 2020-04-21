dictionary_name = {key_1: value_1, key_N: value_N}
dictionary_name = {}
dictionary_name[key]

# Создание и вызов отдельных значений в словаре
contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
jason_phone = contacts['Jason']
carls_phone = contacts['Carl']

print('Dial {} to call Jason'.format(jason_phone))
print('Dial {} to call Carl'.format(carls_phone))

# Замена значения в словаре

contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
contacts['Jason'] = '555-0000'
jason_phone = contacts['Jason']
print('Dial {} to call Jason.'.format(jason_phone))

# Добавление нового значения в словарь
contacts = {'Jason': '555-0123', 'carl': '555-0987'}
contacts['Tony'] = '555-0570'
print(contacts)
print(len(contacts))

# Удаление из словаря

contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
del contacts['Jason']
print(contacts)

# Словари с несколькими значениями
contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}

print('Jason:')
print(contacts['Jason'])
print('Carl:')
print(contacts['Carl'])

# Циклы в словарях
contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}

for number in contacts['Jason']:
    print('Phone: {}.'.format(number))

contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}

if 'Jason' in contacts.keys():
    print("Jason's phone number is:")
    print(contacts['Jason'][0])

if 'Tony' in contacts.keys():
    print("Tony's phone is:")
    print(contacts['Tony'][0])

# Проверка есть ли значение в словаре
contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}

print('555-0987' in contacts.values())
